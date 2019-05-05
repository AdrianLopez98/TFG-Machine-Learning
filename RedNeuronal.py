import pandas as pd
import matplotlib.pyplot as mtp
import numpy as np
import hashlib
import warnings
import CategoricalEncoder
import CombineAtributesAdder
warnings.simplefilter(action='ignore', category=FutureWarning)
casas=pd.read_csv("casas.csv")
#print(casas.head())

#print(housing.info())
#print(housing["ocean_proximity"].value_counts())

#casas["longitude"].hist(bins=50,figsize=(20,20))
#  mtp.show()

def test_set_check(id, test_ratio, hash):

    return hash(np.int64(id)).digest()[-1] < 256 * test_ratio #devuelve el 20% de las veces true, devuelve true si el ultimo bit del hash de ese id es menor que 256(todos los valores posibles)
                                                              #* 0.2 osea se el 20%

def split_train_test_by_id(datos, test_ratio, id_column, hash=hashlib.md5):
    ids = datos[id_column] #guardo en ids el valor de los registros de datos
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))#aplicamos con lambda la funcion que nos devuelve true o false y guardamos los return en una variable
    return datos.loc[~in_test_set], datos.loc[in_test_set]#devuelvo los que son true y los que son false para guardaarlos en sets distintos

casas_con_id = casas.reset_index()   # adds an `index` column
set_entreno, set_test = split_train_test_by_id(casas_con_id, 0.2, "index")

casas_con_id["id"] = casas["longitude"] * 1000 + casas["latitude"] # creamos una columna llamada id a partir de la latitud y la longitud
set_entreno, set_test = split_train_test_by_id(casas_con_id, 0.2, "id")

#print(len(set_entreno), "train +", len(set_test), "test")

#print(set_entreno.head())

casas["income_cat"]=np.ceil(casas["median_income"]/1.5) #con esto reducimos el numero de distritos de ganancias medias lo redondeo a la alta
casas["income_cat"].where(casas["income_cat"]<5,5.0,inplace=True)#todos los distritos que no son menores que 5 los ponemos en 5.0

casas
#vamos a crear los samplings usando sklearn

from sklearn.model_selection import StratifiedShuffleSplit

split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

for entreno_index, test_index in split.split(casas,casas["income_cat"]): #genera una lista de tuplas con los index que devuelve la funcion split
    strat_set_entreno=casas.loc[entreno_index]
    strat_set_test=casas.loc[test_index]

#print(strat_set_test["income_cat"].value_counts() / len(strat_set_test))

for set_ in (strat_set_entreno, strat_set_test):
    set_.drop("income_cat", axis=1, inplace=True)

casas = strat_set_entreno.copy()


import matplotlib.image as mpimg
california_img=mpimg.imread('Imagenes/california.png')#leemos la imagen
#grafica de dispersion con la imagen de california cuadrada de fondo, alpha es la transparencia
ax = casas.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                       s=casas['population']/100, label="Población",
                       c="median_house_value", cmap=mtp.get_cmap("jet"),#jet es el rango de colores
                       colorbar=True, alpha=0.4,
                      )
mtp.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5)
mtp.ylabel("Latitud", fontsize=14,labelpad=15)
mtp.xlabel("Longitud", fontsize=14,labelpad=15)
'''
precios = casas["median_house_value"]
tick_values = np.linspace(precios.min(), precios.max(), 11)
cbar = mtp.colorbar()
cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=14)
#cbar.set_label('Valor Medio', fontsize=16)
'''
mtp.legend(fontsize=16)
#mtp.show()
casas = strat_set_entreno.drop("median_house_value", axis=1) # eliminamos la label objetivo  casas input etiquetas_casas output variable
etiquetas_casas = strat_set_entreno["median_house_value"].copy() #es donde tengo los precios

#vamos a limpiar los datos vacios, total_bedrooms tiene espacios con null
#los rellenamos con datos medios ya que las podriamos eliminar pero perderiamos bastantes datos que si tiene

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

#eliminamos los datos que no son numericos
casas_num = casas.drop('ocean_proximity', axis=1)
#entrenamos los valores numericos para la mediana
imputer.fit(casas_num)
#llena x con la mediana
X = imputer.transform(casas_num)
#creamos un dataframe con los datos
casas_tr = pd.DataFrame(X, columns=casas_num.columns)
#print(casas_tr.info())

#convertimos la proximidad al mar en numeros factorizando, que lo que hace es convertir las categorias a numeros

casas_cat=casas["ocean_proximity"]
#print(casas_cat.head)

casas_cat_encoded, casas_categorias = casas_cat.factorize()
#print(casas_cat_encoded)

#es necesario convertir a one hot encoder para que el paso de la proximidad al oceano a numero no de valores falsos
from sklearn.preprocessing import OneHotEncoder
#print("aqui")
encoder = OneHotEncoder()
casas_cat_1hot = encoder.fit_transform(casas_cat_encoded.reshape(-1,1))
casas_cat_1hot=casas_cat_1hot.toarray()

#print(casas_cat_1hot)
cat_encoder = CategoricalEncoder.CategoricalEncoder(encoding="onehot-dense")
casas_cat_reshaped = casas_cat.values.reshape(-1, 1)
casas_cat_1hot = cat_encoder.fit_transform(casas_cat_reshaped)
#print("el otro")
#print(casas_cat_1hot)
#los algoritmos de ML no trabajan bien con valores muy dispares(alejados) por lo que tenemos que hacer algunas modificaciones(normalizar,escalar) num-min partido de max-min

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


#sklearn no soporta los dataframe por lo que tendremos que trabajar con numpy arrays
import DataFrameSelector

num_attribs = list(casas_num)
cat_attribs = ["ocean_proximity"]

#pipe para numeros
num_pipeline = Pipeline([
        ('selector', DataFrameSelector.DataFrameSelector(num_attribs)),
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombineAtributesAdder.CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])
#pipe para categorias
cat_pipeline = Pipeline([
        ('selector', DataFrameSelector.DataFrameSelector(cat_attribs)),
        ('cat_encoder', CategoricalEncoder.CategoricalEncoder(encoding="onehot-dense")),
    ])

from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
    ])

casas_final=full_pipeline.fit_transform(casas)

#se viene la linear regresion


from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(casas_final, etiquetas_casas)#casas_final son los inputs y el output es etiquetsd_casas que tiene el valor de las casas es el output

#prueba  siempre que queramos hacer una prediccion tenemos que pasar los datos por la pipe
#import InterfazDatos#
#intr=InterfazDatos.InterfazDatos()#
datos_random={"longitude":122,"latitude":38.1,"housing_median_age":41.0,"total_rooms":880.0,"total_bedrooms":129.0,"population":322.0,"households":126.0,"median_income":8.3252,"ocean_proximity":"NEAR BAY"}
datos_random=pd.DataFrame(datos_random,index=[0])
#datos_random=casas.iloc[:1]
etiquetas_random=etiquetas_casas.iloc[:1]
datos_preparados=full_pipeline.transform(datos_random)

#print("Predictions:", lin_reg.predict(datos_preparados))
#print("Actual values",list(etiquetas_random))

#Controlar el square error

from sklearn.metrics import mean_squared_error

predicciones = lin_reg.predict(casas_final)
lin_mse = mean_squared_error(etiquetas_casas, predicciones)
lin_rmse = np.sqrt(lin_mse)
#print(lin_rmse)

#modelo treeregresion

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(casas_final, etiquetas_casas)

predicciones = tree_reg.predict(casas_final)
tree_mse = mean_squared_error(etiquetas_casas, predicciones)
tree_rmse = np.sqrt(tree_mse)
#print(tree_rmse)
#print("Predictions:", tree_reg.predict(datos_preparados))
#print("Actual values",list(etiquetas_random))
#print(datos_random)
#print(datos_preparados)

def predice():#
    return tree_reg.predict(datos_preparados)#
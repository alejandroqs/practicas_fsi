import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Pregunta por pantalla:
graph = raw_input("Show errors graph (y/n): ")
response = str(graph).strip()

#Traduce una lista de etiquetas en un vector de 0's y un 1.
# Por ejemplo: 4 -> [0,0,0,0,1,0,0,0,0,0]
def one_hot(x, n):
    if type(x) == list:
        x = np.array(x)
    x = x.flatten()
    o_h = np.zeros((len(x), n))
    o_h[np.arange(len(x)), x] = 1
    return o_h


#Carga los datos de iris:
data = np.genfromtxt('iris.data', delimiter=",")
np.random.shuffle(data)
x_data = data[:,0:4].astype('f4')
y_data = one_hot(data[:,4].astype(int), 3)

#Codigo para imprimir la tabla de datos:
#print y_data

#print "\nSome samples..."
#for i in range(20):
#    print x_data[i], " -> ", y_data[i]
#print


#Elegimos el numero de entradas (Xi) y las neuronas de la capa de salida:
NUMBER_OF_ENTRIES = 4
OUTPUT_LAYER_NEURONS = 3

#Reservamos memoria para los datos de entrada y la clase:
x = tf.placeholder("float", [None, NUMBER_OF_ENTRIES])
y_ = tf.placeholder("float", [None, OUTPUT_LAYER_NEURONS])

#Elegimos el numero de neuronas en la capa oculta 
#y lo guardamos en una constante:
HIDDEN_LAYER_NEURONS = 4

#Pesos y BIAS de la capa oculta:
hidden_W = tf.Variable(np.float32(np.random.rand(NUMBER_OF_ENTRIES, HIDDEN_LAYER_NEURONS)) * 0.1)
hidden_b = tf.Variable(np.float32(np.random.rand(HIDDEN_LAYER_NEURONS)) * 0.1)

#Pesos y BIAS de la capa externa:
W = tf.Variable(np.float32(np.random.rand(HIDDEN_LAYER_NEURONS, OUTPUT_LAYER_NEURONS)) * 0.1)
b = tf.Variable(np.float32(np.random.rand(OUTPUT_LAYER_NEURONS)) * 0.1)

#Salida de capa oculta:
hidden_y = tf.sigmoid(tf.matmul(x, hidden_W) + hidden_b)

#Salida de capa externa. Resultado:
y = tf.nn.softmax((tf.matmul(hidden_y, W) + b))

#Comprobación de error:
cross_entropy = tf.reduce_sum(tf.square(y_ - y))

#Entrenamiento de neurona (Ajuste de pesos):
train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#Inicializamos variables:
init = tf.initialize_all_variables()

#Iniciamos sesión del TensorFlow: 
sess = tf.Session()
sess.run(init)

#Consola:
print "----------------------"
print "   Start training...  "
print "----------------------"

batch_size = 20

errors = []
for step in xrange(1000):
    for jj in xrange(len(x_data) / batch_size):
        batch_xs = x_data[jj*batch_size : jj*batch_size+batch_size]
        batch_ys = y_data[jj*batch_size : jj*batch_size+batch_size]

        sess.run(train, feed_dict={x: batch_xs, y_: batch_ys})
        if step % 50 == 0:
            error = sess.run(cross_entropy, feed_dict={x: batch_xs, y_: batch_ys})
            errors.append(error)
            print "Iteration #:", step, "Error: ", error
            result = sess.run(y, feed_dict={x: batch_xs})
            for b, r in zip(batch_ys, result):
                print b, "-->", r
            print "----------------------------------------------------------------------------------"


#Grafica:
if response == "y":
    plt.plot(errors)
    plt.show()
            
            
            

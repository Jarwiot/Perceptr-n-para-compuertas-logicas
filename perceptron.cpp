#include <iostream>
using namespace std;


void perceptron(int inputs[4][2], int salidaEsp[4], float pesos[3], float factAprendizaje, int epocas) {
    
    int salida = 0;
    
    for(size_t Epocas = 0; Epocas < epocas; Epocas++) {
        cout << "Epoca " << Epocas + 1 << ":\n";
        for (size_t i = 0; i < 4; i++)
        {
            int x1 = inputs[i][0];
            int x2 = inputs[i][1];
            int y = salidaEsp[i];

            float sum = x1 * pesos[0] + x2 * pesos[1] + pesos[2];
            cout << "  Iteracion " << i + 1 << " -> sum: " << sum << endl;


            if(sum >= 0)
            {
                salida = 1;
            }
            else
            {
                salida = -1;
            }

            //calcular error
            int error = y - salida;

            //actualizar pesos
            pesos[0] = pesos[0] + factAprendizaje * error * x1;
            pesos[1] = pesos[1] + factAprendizaje * error * x2;
            pesos[2] = pesos[2] + factAprendizaje * error;

            cout << "  Pesos-> " << i + 1 << ": Pesos -> [" << pesos[0] << ", " << pesos[1] << ", " << pesos[2] << "]\n";

        }
    }
}



int main() {
    //Pesos
    float pesos[3] = {0, 0, 0};


    //Entradas
    int inputs[4][2] = 
    {
        {2,  1},
        {1, -1},
        {2, -2},
        {3,  1}
    };

    int salidaEsp[4] = {1, -1, -1, 1};

    float factAprendizaje = 1;
    int epocas = 10;

    perceptron(inputs, salidaEsp, pesos, factAprendizaje, epocas);

    // Pesos finales
    cout << "\nPesos finales: [" << pesos[0] << ", " << pesos[1] << ", " << pesos[2] << "]\n";



    return 0;
}
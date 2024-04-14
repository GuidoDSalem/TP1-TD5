#include <string>
#include <iostream>
#include <fstream>
#include "include/json.hpp"
#include "include/Core.hpp"
#include "include/backTracking.hpp"

// Para libreria de JSON.
using namespace nlohmann;

using namespace std;

int main(int argc, char** argv) {
    std::string instance_name = "../../data/titanium.json";
    std::cout << "Reading file " << instance_name << std::endl;
    std::ifstream input(instance_name);

    json instance;
    input >> instance;
    input.close();
    std::cout << std::endl<< "________instance__________" << std::endl;
    printJson(instance);

    float a = 2.3;
    float b = 4.4;
    float c = 5.5;
    float d = 6.6;
    vector<float> vector1;
    vector1.push_back(a);
    vector1.push_back(b);
    vector1.push_back(c);
    vector1.push_back(d);
    printVector(&vector1);
    printVector(&vector1,"AAA");

    printJson(instance);

    /*
    std::cout << std::endl<< "________errorbp_____test_____" << std::endl;
    //copiamos los x values del json , al pedo guido puso dos nombres de fucniones iguales pero ahc ebasicamente esto de una
    vector<float> x_values = getJsonValues(instance,"x");
    vector<float> y_values = getJsonValues(instance,"y");

    //hacemos un grid de 6x6
    vector<float> gridX;
    linspace(gridX, minJson(instance,"x"), maxJson(instance,"x"), 6);
    printVector(&gridX,"gridX");

    vector<float> gridY;
    linspace(gridY, minJson(instance,"y"), maxJson(instance,"y"), 6);
    printVector(&gridY,"gridY");

    //depsues que tenemos el grid artificialmente hacemos los breakpoints, que en python nos dieron error 0
    
    vector<float> ys = {0.0 , 0.6, 1.2, 3.0, 3.0, 0.0};
    
    vector<float> xs = {0.0, 0.6, 1.2, 1.8, 2.4, 3.0};
   
    float error = errorBreakPoint(xs,ys,instance);

    cout << error <<endl;

    */
     
    std::cout << std::endl<< "________bt____test______" << std::endl;
    int m = 6;
    int n = 6;
    int k = 6;

    Result_bt result_bt = backTracking(m,n,k,instance);
    cout << "BACKTRACKING ASNWER:" << endl;
    printResult(result_bt);


    // float pendiente(float x1, float y1, float x2, float y2);
    // float error(float m, float x1, float y1, float xd, float yd);
    // float errorAB(float xa, float ya, float xb, float yb, const json &data);
    void pepe();

    int K = instance["n"];
    
    int N = 5;

    std::cout << K << std::endl;

    // Aca empieza la magia.

    // Ejemplo para guardar json.
    // Probamos guardando el mismo JSON de instance, pero en otro archivo.
    std::ofstream output("test_output.out");

    output << instance;
    output.close();

    return 0;
}
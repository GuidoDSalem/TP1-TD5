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
    std::string instance_name = "../../data/toy_instance.json";
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

    vector<float> gridX;
    linspace(&gridX, min(vector1), max(vector1), 5);
    printVector(&gridX,"gridX");

    vector<float> vectorLinspace;
    linspace(&vectorLinspace, 0, 5, 5);
    printVector(&vectorLinspace,"LinspaceX");

    printJson(instance);
    std::cout << std::endl<< "________error bp__________" << std::endl;
    

    std::cout << std::endl<< "________bt__________" << std::endl;


    ResultT_bt result_bt = backTracking(6,6,4,instance);
    printResult(result_bt);


    // float pendiente(float x1, float y1, float x2, float y2);
    // float error(float m, float x1, float y1, float xd, float yd);
    // float errorAB(float xa, float ya, float xb, float yb, const json &data);
    void pepe();

    int K = instance["n"];
    int m = 6;
    int n = 6;
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
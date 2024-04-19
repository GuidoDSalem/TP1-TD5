#include <string>
#include <iostream>
#include <fstream>
#include "include/json.hpp"
#include "include/Core.hpp"
#include "include/backTracking.hpp"
#include "include/pDinamica.hpp"

// Para libreria de JSON.
using namespace nlohmann;

using namespace std;

int main(int argc, char** argv) {
    std::string instance_name = "../../data/optimistic_instance.json";
    std::cout << "Reading file " << instance_name << std::endl;
    std::ifstream input(instance_name);

    json instance;
    input >> instance;
    input.close();
    /*
    std::cout << std::endl<< "________core_tests__________" << std::endl;
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

    // float pendiente(float x1, float y1, float x2, float y2);
    // float error(float m, float x1, float y1, float xd, float yd);
    // float errorAB(float xa, float ya, float xb, float yb, const json &data);
    void pepe();


   
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
    std::vector<std::string> fileNames = {
        "../../data/aspen_simulation.json",
        "../../data/ethanol_water_vle.json",
        "../../data/optimistic_instance.json",
        "../../data/titanium.json",
        "../../data/toy_instance.json"
       
    };
    std::vector<int> breakpoints = {2,3,4,5,6}; 
    std::vector<int> ms = {6}; 
    std::vector<int> ns = {6};

    for (const auto& fileName : fileNames) {
        
        // Abrir el archivo
        std::ifstream input(fileName);
        
        if (!input.is_open()) {
            std::cerr << "No se pudo abrir el archivo " << fileName << std::endl;
            continue;  // Si no se abrio ir al siguiente archivo
        }

       
        nlohmann::json instance;
        input >> instance;
        input.close();
    
        std::cout << "-----------------------" << fileName << "----------- " << std::endl;
        
        for (int m : ms) {
            for (int n : ns) {
                for (int k : breakpoints) {
                    
                    std::cout << "\nTest con: m=" << m << ", n=" << n << ", k=" << k << std::endl;

                    Result_bt result_bt = backTracking(m, n, k, instance);
                    std::cout << "\nBACKTRACKING RESPUESTA:" << std::endl;
                    printResult(result_bt);

                    Result_bt result_pd = pDinamica(m, n, k, instance);
                    std::cout << "\nPDINAMICA RESPUESTA:" << std::endl;
                    printResult(result_pd);

                    std::cout << "\n_________________________\n" << std::endl;
                }
            }
        }
        

    }


    
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
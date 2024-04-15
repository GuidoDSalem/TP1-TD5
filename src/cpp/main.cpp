#include <string>
#include <iostream>
#include <fstream>
#include "include/json.hpp"
<<<<<<< HEAD
#include "include/functions.hpp"

=======
#include "include/Core.hpp"
#include "include/Resultado.hpp"
#include "include/FuerzaBruta.hpp"
>>>>>>> b83eee88c43ad4ed28a09d8017bff48c0ebd7824

// Para libreria de JSON.
using namespace nlohmann;
using namespace std;

int main(int argc, char** argv) {
    std::string instance_name = "../../data/titanium.json";
    std::cout << "Reading file " << instance_name << std::endl;
    std::ifstream input(instance_name);
    std::cout<<"START..."<<endl;
    json data;
    input >> data;
    input.close();

    Resultado res = Resultado();
    fuerzaBruta(res ,6 ,6 ,5,data);

        // float pendiente(float x1, float y1, float x2, float y2);
        // float error(float m, float x1, float y1, float xd, float yd);
        // float errorAB(float xa, float ya, float xb, float yb, const json &data);
        

    int K = data["n"];
    int m = 6;
    int n = 6;
    int N = 5;

    std::cout << K << std::endl;

    // Aca empieza la magia.

    // Ejemplo para guardar json.
    // Probamos guardando el mismo JSON de instance, pero en otro archivo.
    // std::ofstream output("test_output.out");

    // output << instance;
    // output.close();

    return 0;
}
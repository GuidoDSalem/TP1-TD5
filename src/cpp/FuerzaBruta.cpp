#include "include/FuerzaBruta.hpp"


void fuerzaBruta(Resultado &res, int m, int n,int k, const json &data){
    std::vector<float> grillaX;
    std:vector<float> grillaY;

    linspace(&grillaX,min(data,"x"),max(data,"y"),k);
    linspace(&grillaY, min(data, "x"), max(data, "y"), k);

    printVector(&grillaX,"grillaX");
    printVector(&grillaY, "grillaY");
}
float fuerzaBrutaRecursiva(){

}
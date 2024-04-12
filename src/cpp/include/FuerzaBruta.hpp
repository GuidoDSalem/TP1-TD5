#ifndef FUERZA_BRUTA
#define FUERZA_BRUTA

#include <string>
#include <iostream>
#include <vector>
#include "json.hpp"
#include "Resultado.hpp"
#include "Core.hpp"
using namespace nlohmann;
using namespace std;

void fuerzaBruta(Resultado &res,int m, int n,const json &data);
float fuerzaBrutaRecursiva();


#endif//UERZA_BRUTA
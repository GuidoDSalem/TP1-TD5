#ifndef FUERZA_BRUTA
#define FUERZA_BRUTA

#include <string>
#include <iostream>
#include <vector>
#include "json.hpp"
#include "Resultado.hpp"
#include "Core.hpp"
#include <chrono>
using namespace nlohmann;
using namespace std;
using namespace std::chrono;

void fuerzaBruta(Resultado &res,int m, int n,int k,const json &data);

// float fuerzaBrutaRecursiva(vector<float> &gridX, vector<float> &gridY, vector<float> &xs, vector<float> &ys, vector<float> &res,int k,float bestError,const json &datos);

#endif//UERZA_BRUTA
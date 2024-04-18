#ifndef PROGRAMACION_DINAMICA
#define PROGRAMACION_DINAMICA

#include <string>
#include <iostream>
#include <vector>
#include <tuple>
#include <chrono>
#include <cmath>
#include <unordered_map>
#include <map>

#include "json.hpp"
#include "Resultado.hpp"
#include "Core.hpp"

using namespace nlohmann;
using namespace std;
using namespace std::chrono;


Result_bt pDinamica(int m, int n, int k, const json &data);
float pDinamicaRecursiva(const vector<float> &gridX, const vector<float> &gridY, vector<float> &resX, vector<float> &resY, vector<float> &bestResY, float &bestError, const json &datos);
float errorBreakPoints_dinamico(const vector<float>& listaX, const vector<float>& listaY, const json& datos);

#endif//PROGRAMACION_DINAMICA
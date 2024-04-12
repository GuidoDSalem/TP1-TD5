#ifndef BACK_TRACKING
#define BACK_TRACKING

#include <string>
#include <iostream>
#include <vector>
#include <tuple>
#include <chrono>

#include "json.hpp"
#include "Resultado.hpp"
#include "Core.hpp"
using namespace nlohmann;
using namespace std;

tuple<float, vector<float>, float> backTracking(Resultado &res,int m, int n,const json &data);
float backTrackingRecursiva(vector<float> gridX, vector<float> gridY, vector<float> resX, vector<float> resY, vector<float> bestResY, float bestError, const json &data);


#endif//back tracking
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


ResultT_bt backTracking(int m, int n, int k, const json &data);
float backTrackingRecursiva(vector<float> gridX, vector<float> gridY, vector<float> resX, vector<float> resY, vector<float> bestResY, float bestError, const json &data);


#endif//back tracking
#ifndef BACK_TRACKING
#define BACK_TRACKING

#include <string>
#include <iostream>
#include <vector>
#include <tuple>
#include <chrono>
#include <cmath>

#include "json.hpp"
#include "Resultado.hpp"
#include "Core.hpp"

using namespace nlohmann;
using namespace std;
using namespace std::chrono;


Result_bt backTracking(int m, int n, int k, const json &data);
float backTrackingRecursiva(const vector<float> &gridX, const vector<float> &gridY, vector<float> &resX, vector<float> &resY, vector<float> &bestResY, float &bestError, const json &datos);


#endif//back tracking
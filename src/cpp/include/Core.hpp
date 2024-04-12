#ifndef CORE
#define CORE

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "json.hpp"
using namespace nlohmann;
using namespace std;

void printJson(json &data);
void printVector(vector<float> *v);
void linspace(vector<float> *v, float min, float max, int m);
float pendiente(float x1, float y1, float x2, float y2);
float error(float m,float x1,float y1,float xd, float yd);
float errorAB(float xa,float ya, float xb, float yb,const json &data);
void pepe();


#endif//CORE
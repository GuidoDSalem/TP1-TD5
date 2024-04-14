#ifndef CORE
#define CORE

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "json.hpp"
using namespace nlohmann;
using namespace std;

struct ResultT_bt {
    float roundedBestError;
    vector<float> bestRes;
    float roundedTotalTime;
};

void printJson(json &data);
vector<float> getJsonValues(const json& data, const string& key);
float min(vector<float> &v);
float max(vector<float> &v);
float minJson(const json &data,const string s);
float maxJson(const json &data, const string s);
void printVector(vector<float> *v);
void printVector(vector<float> *v,string msg);
void printResult(const ResultT_bt& result);
void linspace(vector<float>& v, float min, float max, int m);
float pendiente(float x1, float y1, float x2, float y2);
float error(float m,float x1,float y1,float xd, float yd);
float errorAB(float xa, float ya, float xb, float yb, const json &data);
float errorBreakPoint(const vector<float> &xs,const vector<float> &ys, const json &data);
void pepe();
void listasCombinatorias(const vector<float>& lista, vector<float>& subconjuntos, vector<vector<float>>& lista_subconjuntos, int k);

#endif//CORE
#ifndef CORE
#define CORE

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include "json.hpp"
using namespace nlohmann;
using namespace std;

struct Result_bt {
    float BestError;
    vector<float> bestSubGrid;
    vector<float> bestRes;
    float TotalTime;
};

struct PairHash {
    //función de hash que toma un par constante de pares de floats como argumento y devuelve un valor de hash 
    std::size_t operator () (const std::pair<std::pair<float, float>, std::pair<float, float>>& p) const {
        // Agaarra el primer par, punto A
        std::size_t h1 = std::hash<float>{}(p.first.first);
        std::size_t h2 = std::hash<float>{}(p.first.second);
        // Agarra el segundo par, punto B
        std::size_t h3 = std::hash<float>{}(p.second.first);
        std::size_t h4 = std::hash<float>{}(p.second.second);

        // Combina los hashes
        return h1 ^ h2 ^ h3 ^ h4;
    }
};


void printJson(json &data);
vector<float> getJsonValues(const json& data, const string& key);
float min(vector<float> &v);
float max(vector<float> &v);
float minJson(const json &data,const string s);
float maxJson(const json &data, const string s);
void printVector(vector<float> *v);
void printVector(vector<float> *v,string msg);
void printResult(const Result_bt& result);
void linspace(vector<float>& v, float min, float max, int m);
float pendiente(float x1, float y1, float x2, float y2);
float error(float m,float x1,float y1,float xd, float yd);
float errorAB(float xa, float ya, float xb, float yb, const json &data);
float errorBreakPoint(const vector<float> &xs,const vector<float> &ys, const json &data);
void pepe();
void listasCombinatorias(const vector<float>& lista, vector<float>& subconjuntos, vector<vector<float>>& lista_subconjuntos, int k);

#endif//CORE
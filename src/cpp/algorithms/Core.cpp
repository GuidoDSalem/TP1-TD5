#include <string>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include "functions.hpp"
#include <cmath>
#include <stdexcept>

using namespace std;


float error(int m,int x1,int y1,int xd,int yd){
    int yPred = m * (xd - x1) + y1;
    return abs(yPred - yd);
};

float pendiente(int x1,int y1,int x2,int y2){
    if(x2 == x1) { 
        throw std::runtime_error("Los dos puntos tienen la misma X -> No tiene pendiente!!");
    }
    int m = (y2 - y1) / (x2 - x1);
    return m;
};

//estoy en esta
float errorAB(int xa,int ya,int, int xb,int yb,const vector<pair<double, double>>& datos){
    if(xa == xb) {
        return 100000000;
    }

    float m = pendiente(xa, ya, xb, yb);
    int i = 0;
    double errorAcumulado = 0;

    // Assuming datos is sorted by x value
    if(datos.front().first > xb) {
        return 0;
    }

    while(datos[i].first < xa) {
        ++i;
        if (i >= datos.size()) break; // Safety check to prevent out-of-bounds access
    }

    while(i < datos.size() && datos[i].first < xb) {
        errorAcumulado += error(m, xa, ya, datos[i].first, datos[i].second);
        ++i;
    }

    return errorAcumulado;
};

float errorBreakPoints(vector<int> listaX,vector<int> listaY,datos){

};

void pepe(){
    int x =3;
};



void plot_puntos_y_linea(data,vector<int> linea_x,vector<int> linea_y,int m,int n,string algo,float error,float tiempo){

};

void listasCombinatorias(vector<int> list,vector<int> subconjuntos,vector<int> lista_subconjuntos,int k){

};






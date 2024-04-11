#ifndef FUNCTIONS_HPP
#define FUNCTIONS_HPP

#include <string>
#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

//las de core 
float error(int m,int x1,int y1,int xd,int yd);

float pendiente(int x1,int y1,int x2,int y2);

float errorAB(int xa,int ya,int, int xb,int yb, datos);

float errorBreakPoints(vector<int> listaX,vector<int> listaY,datos);

void pepe();

void plot_puntos_y_linea(data,vector<int> linea_x,vector<int> linea_y,int m,int n,string algo,float error,float tiempo);

void listasCombinatorias(vector<int> list,vector<int> subconjuntos,vector<int> lista_subconjuntos,int k);

//fuerza bruta recursiva
tuple<float,vector<int>,float> fuerzaBruta(int m,int n,int k,const &datos);

float fuerzaBrutaRecursiva(vector<int> gridX,vector<int> gridY,vector<int> xs,vector<int> ys,vector<int> res,float bestError,const &datos);

//backtracking 

//programacion dinamica


#endif // FUNCTIONS_HPP

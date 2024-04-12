#include "include/Core.hpp"

void printJson(json &data){
    std::cout<<"X: "<< data["x"] <<"\n"<<std::endl;
    std::cout<<"Y: "<< data["y"] <<"\n"<<std::endl;
};

void printVector(vector<float> *v,string msg = ''){

    for(int i=0; i< v->size(); i++){

    }
}

void linspace(vector<float>* v,float min, float max, int m){
    if(min == max){
        return;
    }
    float dif = max - min;
    dif = dif / m;
    v->push_back(min);
    for(int i=1; i < m;i++){
        v->push_back(min + dif*i);
    }

}
void printBreakPoints(vector<float> xs, vector<float> ys){
    std::cout<<"BREAK POINTS: ";
    for(int i=0; i < xs.size()-1;i++){
        std::cout<<"["<<xs[i]<<","<<ys[i]<<"],";
    }
    std::cout << "[" << xs[xs.size()] << "," << ys[ys.size()] << "]"<<std::endl;
}
float pendiente(float x1, float y1, float x2, float y2){
    return (y2 - y1)/(x2 - x1);
}
float error(float m, float x1, float y1, float xd, float yd){
    float y_pred = m * (xd - x1) + y1;
    float res = yd - y_pred;
    if(res > 0){
        return res;
    }
    else{
        return res * -1;
    }
}
float errorAB(float xa, float ya, float xb, float yb, const json &data){
    
    int i = 0;
    if(data["x"][i] > xb){
        return (float)100000001;
    }

    float m = pendiente(xa,ya,xb,yb);

    while( xa > data["x"][i]){
        i++;
    }
    float errorAcumulado = 0;
    while (data["x"][i] < xb && i < data["x"].size()){
        errorAcumulado += error(m, xa, ya, data["x"][i], data["y"][i]);
    }

    return errorAcumulado;
}
void pepe(){
    int x = 3;
}
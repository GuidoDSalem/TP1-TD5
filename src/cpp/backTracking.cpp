#include "include/backTracking.hpp"

struct Result {
    float roundedBestError;
    vector<float> bestRes;
    float roundedTotalTime;
};


Result backTracking(int m, int n,const json &data){
    //empezar el tiempo:
    auto start = chrono::steady_clock::now();

    //creamos grilla de datos 
    vector<float> gridX;
    vector<float> gridY;
    linspace(gridX, min(data,x), max(data, x), m);
    linspace(gridY, min(data,y), max(data, y), m);

    //sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    vector<float> conjunto_medio = gridX;
    conjunto_medio.erase(conjunto_medio.begin());
    conjunto_medio.pop_back();

    //creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    vector<vector<float>> listas_medio;
    listasCombinatorias(conjunto_medio, vector<float>(), listas_medio, k-2);

    //agregamos el primer y ultimo elemento de la lista
    for (auto& lista : listas_medio) {
        lista.insert(lista.begin(), gridX[0]);
        lista.push_back(gridX.back());
    }

    vector<float> bestRes;
    vector<float> bestSubGridX;
    double bestError = 100000000000001;


    vector<int> bestRes(k, gridY.back()); 

    //con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for (const auto& subGridX : listas_medio) {
        
        vector<int> res(subGridX.size(), gridY[0]); 

        double errorActual = backTrackingRecursiva(subGridX, gridY, vector<int>(), vector<int>(), res, bestError, data);

        if (errorActual < bestError) {
            bestSubGridX = subGridX;
            bestError = errorActual;
            bestRes = res;
        }
    }

    auto end = chrono::steady_clock::now();

    auto totalTime = chrono::duration_cast<chrono::milliseconds>(end - start);

    auto milliseconds = duration.count();

    cout << "GridY: " << endl;
    printVector(gridY);
    cout << "Tiempo: " << milliseconds << ", Function: " << bestRes << endl;

    Result result = {(round(bestError * 100) / 100), bestRes, (round(totalTime * 100) / 100)};
    
    return result;
};

float backTrackingRecursiva(vector<float> gridX, vector<float> gridY, vector<float> resX, vector<float> resY, vector<float> bestResY, float bestError, const json &data){

};

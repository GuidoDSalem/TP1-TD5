#include "include/backTracking.hpp"


ResultT_bt backTracking(int m, int n, int k ,const json &data){
    //empezar el tiempo:
    auto start = std::chrono::steady_clock::now();
    
    //creamos grilla de datos 
    vector<float> gridX;
    vector<float> gridY;
    linspace(&gridX, min(data,"x"), max(data, "x"), m);
    linspace(&gridY, min(data,"y"), max(data, "y"), n);

    //sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    vector<float> conjunto_medio = gridX;
    if (!conjunto_medio.empty()) {
        conjunto_medio.erase(conjunto_medio.begin());
        conjunto_medio.pop_back();
    }
   
    //creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    vector<vector<float>> listas_medio;
    vector<float> subconjunto;
    listasCombinatorias(conjunto_medio, subconjunto, listas_medio, k-2);

    //agregamos el primer y ultimo elemento de la lista
    for (auto& lista : listas_medio) {
        lista.insert(lista.begin(), gridX[0]);
        lista.push_back(gridX.back());
    }

    vector<float> bestSubGridX;
    double bestError = 100000000000001;


    vector<float> bestRes(k, gridY.back()); 

    //con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for (const auto& subGridX : listas_medio) {
        
        vector<float> res(subGridX.size(), gridY[0]); 
        vector<float> resX;
        vector<float> resY;

        double errorActual = backTrackingRecursiva(subGridX, gridY, resX, resY, res, bestError, data);

        if (errorActual < bestError) {
            bestSubGridX = subGridX;
            bestError = errorActual;
            bestRes = res;
        }
    }

    auto end = std::chrono::steady_clock::now();

    auto totalTime =std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();


    cout << "GridY: " << endl;
    printVector(&gridY);
    cout << "Tiempo: " << totalTime << endl;
    cout << ", Function: " << endl;
    printVector(&bestRes);

    ResultT_bt result = {static_cast<float>(round(bestError * 100) / 100), bestRes, static_cast<float>(round(totalTime * 100) / 100)};

    return result;
};

float backTrackingRecursiva(const vector<float> gridX, const vector<float> gridY, vector<float> resX, vector<float> resY, vector<float> bestResY, float bestError, const json &datos){    
    // Poda de optimalidad
    if (errorBreakPoint(resX, resY, datos) > errorBreakPoint(gridX, bestResY, datos)) {
        return errorBreakPoint(resX, resY, datos);
    }

    // Caso Base
    if (gridX.size() == resX.size()) {
        float errorBP = errorBreakPoint(resX, resY, datos);
        
        // errorActual calculation can be skipped as it is already calculated

        if (errorBP < bestError) {
            bestResY.clear();
            bestResY = resY;
            std::cout << "RES: ";
            for (const auto& elem : bestResY) {
                std::cout << elem << " ";
            }
            std::cout << ", ERROR: " << errorBP << std::endl;
            bestError = errorBP;
        }

        return bestError;
    }

    // Caso recursivo
    size_t i = resX.size();
    resX.push_back(gridX[i]);
    float currentBestError = bestError;
    
    for (const auto& j : gridY) {
        resY.push_back(j);
        float error = backTrackingRecursiva(gridX, gridY, resX, resY, bestResY, currentBestError, datos);
        if (error < currentBestError) {
            currentBestError = error;
        }
        resY.pop_back();
    }

    resX.pop_back();

    return currentBestError;
}
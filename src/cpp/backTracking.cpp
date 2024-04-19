#include "include/backTracking.hpp"

float backTrackingRecursiva(const vector<float> &gridX,
                            const vector<float> &gridY,
                            vector<float> &resX,
                            vector<float> &resY,
                            vector<float> &bestResY,
                            float &bestError,
                            const json &datos)
{

    // Poda de optimalidad
    if (resX.size() != 0)
    {
        float errorActual = errorBreakPoint(resX, resY, datos);
        if (errorActual > bestError)
        {
            return errorActual;
        }
    }

    // Caso Base
    if (gridX.size() == resX.size())
    {
        float errorBP = errorBreakPoint(resX, resY, datos);

        if (errorBP < bestError)
        {
            bestResY.clear();
            bestResY = resY;
            bestError = errorBP;
        }

        return bestError;
    }

    size_t i = resX.size();
    resX.push_back(gridX[i]);
    float currentBestError = bestError;

    // Caso recursivo
    for (const auto &j : gridY)
    {
        resY.push_back(j);
        float error = backTrackingRecursiva(gridX, gridY, resX, resY, bestResY, currentBestError, datos);
        if (error < currentBestError)
        {
            currentBestError = error;
        }
        resY.pop_back();
    }

    resX.pop_back();

    return currentBestError;
}

Result_t backTracking(int m, int n, int k, const json &data)
{
    // empezar el tiempo:
    auto inicio = high_resolution_clock::now();

    // creamos grilla de datos
    vector<float> gridX;
    vector<float> gridY;
    try
    {
        linspace(gridX, minJson(data, "x"), maxJson(data, "x"), m);
        linspace(gridY, minJson(data, "y"), maxJson(data, "y"), n);
    }
    catch (const std::invalid_argument &e)
    {
        exit(1);
    }

    printVector(&gridX, "GRID X: ");
    printVector(&gridY, "GRID Y: ");

    // sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    vector<float> conjunto_medio = gridX;
    if (!conjunto_medio.empty())
    {
        conjunto_medio.erase(conjunto_medio.begin());
        conjunto_medio.pop_back();
    }

    // creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    vector<vector<float>> listas_medio;
    vector<float> subconjunto;
    listasCombinatorias(conjunto_medio, subconjunto, listas_medio, k - 2);

    // agregamos el primer y ultimo elemento de la lista
    for (auto &lista : listas_medio)
    {
        lista.insert(lista.begin(), gridX[0]);
        lista.push_back(gridX.back());
    }

    vector<float> bestSubGridX;
    float bestError = 100000000000001.0f;
    vector<float> bestRes(k, gridY.back());

    // con cada subgrilla probamos backtracking recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for (const auto &subGridX : listas_medio)
    {

        vector<float> res(subGridX.size(), gridY[0]);
        vector<float> resX;
        vector<float> resY;

        float errorActual = 100000000000001.0f;
        errorActual = backTrackingRecursiva(subGridX, gridY, resX, resY, res, bestError, data);

        if (errorActual < bestError)
        {
            bestSubGridX = subGridX;
            bestError = errorActual;
            bestRes = res;
        }
    }

    // calculamos el tiempo
    auto fin = high_resolution_clock::now();
    double totalTime = (double)duration_cast<duration<double>>(fin - inicio).count();

    // devolvemos un struct con todas las respuestas
    Result_t result = {bestError, bestSubGridX, bestRes, static_cast<float>(totalTime)};

    return result;
}

#include "include/pDinamica.hpp"
float errorBreakPoints_dinamico(const vector<float> &listaX,
                                const vector<float> &listaY,
                                const json &datos,
                                unordered_map<pair<pair<float, float>, pair<float, float>>, float, PairHash> &DiccionarioDeErrores)
{
    float errorTotal = 0;

    for (size_t i = 0; i < listaX.size() - 1; ++i)
    {
        // Elegimos 2 puntos a y b cada uno de estos tiene un punto (x,y)
        // en la clave guardamos estos dos puntos (xa,ya),(xb,yb) con el error como valor de la clave

        auto clave = make_pair(make_pair(listaX[i], listaY[i]), make_pair(listaX[i + 1], listaY[i + 1]));

        // Si la clave está en el diccionario, la devolvemos, sino se calcula y se guarda en el diccionario
        if (DiccionarioDeErrores.find(clave) != DiccionarioDeErrores.end())
        {
            errorTotal += DiccionarioDeErrores[clave];
        }
        else
        {
            float error_actual = errorAB(listaX[i], listaY[i], listaX[i + 1], listaY[i + 1], datos);
            DiccionarioDeErrores[clave] = error_actual;
            errorTotal += error_actual;
        }
    }

    return errorTotal;
}

float pDinamicaRecursiva(const vector<float> &gridX,
                         const vector<float> &gridY,
                         vector<float> &resX,
                         vector<float> &resY,
                         vector<float> &bestResY,
                         float &bestError,
                         const json &datos,
                         unordered_map<pair<pair<float, float>, pair<float, float>>, float, PairHash> &DiccionarioDeErrores)
{

    // Poda de optimalidad
    if (resX.size() != 0)
    {
        if (errorBreakPoints_dinamico(resX, resY, datos, DiccionarioDeErrores) > errorBreakPoints_dinamico(gridX, bestResY, datos, DiccionarioDeErrores))
        {
            return errorBreakPoints_dinamico(resX, resY, datos, DiccionarioDeErrores);
        }
    }

    // Caso Base
    if (gridX.size() == resX.size())
    {
        float errorBP = errorBreakPoints_dinamico(resX, resY, datos, DiccionarioDeErrores);

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
        errorBreakPoints_dinamico(resX, resY, datos, DiccionarioDeErrores);
        float error = pDinamicaRecursiva(gridX, gridY, resX, resY, bestResY, currentBestError, datos, DiccionarioDeErrores);
        if (error < currentBestError)
        {
            currentBestError = error;
        }
        resY.pop_back();
    }

    resX.pop_back();

    return currentBestError;
}

Result_t pDinamica(int m, int n, int k, const json &data)
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

    // Creo el diccionario vacio
    unordered_map<pair<pair<float, float>, pair<float, float>>, float, PairHash> DiccionarioDeErrores;

    // con cada subgrilla probamos PDINAMICA recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for (const auto &subGridX : listas_medio)
    {

        vector<float> temp_res(subGridX.size(), gridY[0]);
        vector<float> resX;
        vector<float> resY;

        float errorActual = 100000000000001.0f;
        errorActual = pDinamicaRecursiva(subGridX, gridY, resX, resY, temp_res, bestError, data, DiccionarioDeErrores);

        if (errorActual < bestError)
        {
            bestSubGridX = subGridX;
            bestError = errorActual;
            bestRes = temp_res;
        }
    }

    // calculamos el tiempo
    auto fin = high_resolution_clock::now();
    double totalTime = (double)duration_cast<duration<double>>(fin - inicio).count();

    // devolvemos un struct con todas las respuestas
    Result_t result = {bestError, bestSubGridX, bestRes, static_cast<float>(totalTime)};

    return result;
}

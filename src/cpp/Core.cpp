#include "include/Core.hpp"

void printJson(json &data)
{
    std::cout << "X: " << data["x"] << "\n"
              << std::endl;
    std::cout << "Y: " << data["y"] << "\n"
              << std::endl;
}

float min(vector<float> &v)
{
    float menor = 100000000;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i] < menor)
        {
            menor = v[i];
        }
    }
    return menor;
}

float max(vector<float> &v)
{
    float mayor = 100000000;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i] > mayor)
        {
            mayor = v[i];
        }
    }
    return mayor;
}
float minJson(const json &data, const string s)
{
    if (data[s].empty())
    {
        throw std::invalid_argument("No hay nada");
    }

    float minimo = data[s][0];
    for (size_t i = 1; i < data[s].size(); i++)
    {
        if (data[s][i] < minimo)
        {
            minimo = data[s][i];
        }
    }
    return minimo;
}
float maxJson(const json &data, const string s)
{
    if (data[s].empty())
    {
        throw std::invalid_argument("No hay nada");
    }

    float maximo = data[s][0];
    for (size_t i = 1; i < data[s].size(); i++)
    {
        if (data[s][i] > maximo)
        {
            maximo = data[s][i];
        }
    }
    return maximo;
}

void printVector(vector<float> *v)
{
    std::cout << "VECTOR: [";
    for (int i = 0; i < v->size() - 1; i++)
    {
        std::cout << (*v)[i] << ", ";
    }
    std::cout << v->back();
    std::cout << "]";
    std::cout << endl;
}
void printVector(vector<float> *v, string msg)
{
    std::cout << "VECTOR-" << msg << ": [";
    for (int i = 0; i < v->size() - 1; i++)
    {
        std::cout << (*v)[i] << ", ";
    }
    std::cout << (*v)[v->size() - 1];
    std::cout << " ]";
    std::cout << endl;
}

void printResult(const Result_t &result)
{
    std::cout << "Best Error: " << result.BestError << std::endl;
    std::cout << "ResX: [ ";
    for (const auto &value : result.bestSubGrid)
    {
        std::cout << value << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << "ResY: [ ";
    for (const auto &value : result.bestRes)
    {
        std::cout << value << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << "Total Time: " << result.TotalTime << std::endl;
}

void linspace(std::vector<float> &v, float min, float max, int m)
{
    if (min == max)
    {
        std::cout << "ERROR-linspace: Min == MAX -> esto no puede pasar" << std::endl;
        return;
    }

    float dif = (max - min) / (m - 1);
    for (int i = 0; i < m; i++)
    {
        v.push_back(min + dif * i);
    }
}

void printBreakPoints(vector<float> xs, vector<float> ys)
{
    std::cout << "BREAK POINTS: ";
    for (int i = 0; i < xs.size() - 1; i++)
    {
        std::cout << "[" << xs[i] << "," << ys[i] << "],";
    }
    std::cout << "[" << xs[xs.size()] << "," << ys[ys.size()] << "]" << std::endl;
}

float pendiente(float x1, float y1, float x2, float y2)
{
    return (y2 - y1) / (x2 - x1);
}

float error(float m, float x1, float y1, float xd, float yd)
{
    float y_pred = m * (xd - x1) + y1;
    float res = yd - y_pred;
    return abs(res);
}

float errorAB(float xa, float ya, float xb, float yb, const json &data)
{

    int i = 0;
    if (xa > xb)
    {
        std::cout << "ERROR errorAB: Xa > Xb -> Noesto no puede pasar";
        return 100000001;
    }

    // i = 0
    float errorAcumulado = 0;
    float m = pendiente(xa, ya, xb, yb);

    if (i == data["x"].size())
    {
        return errorAcumulado;
    }

    if (data["x"][i] < xa)
    {

        while (i < data["x"].size() && data["x"][i] < xa)
        {
            i++;
        }
        // i = 0
    }
    else if (data["x"][i] > xb)
    {
        return 0;
    }
    /*  Lo que tenia guido

    if (data["x"][i] < xa){

        while (data["x"][i] < xa)
        {
            i++;
        }

    }
    // i = 0
    else if (data["x"][i] > xb){
        return 0;
    }
    */
    while (data["x"][i] < xb && i < data["x"].size())
    {
        errorAcumulado += error(m, xa, ya, data["x"][i], data["y"][i]);
        i++;
    }

    return errorAcumulado;
}

float errorBreakPoint(const vector<float> &xs, const vector<float> &ys, const json &data)
{
    float errorAcumulado = 0;

    for (int i = 0; i < xs.size() - 1; i++)
    {
        errorAcumulado += errorAB(xs[i], ys[i], xs[i + 1], ys[i + 1], data);
    }

    return errorAcumulado;
}

void pepe()
{
    int x = 3;
}

void listasCombinatorias(const vector<float> &lista, vector<float> &subconjuntos, vector<vector<float>> &lista_subconjuntos, int k)
{
    if (k == 0)
    {
        lista_subconjuntos.push_back(subconjuntos);
        return;
    }
    if (lista.empty())
    {
        return;
    }

    subconjuntos.push_back(lista[0]);
    listasCombinatorias(vector<float>(lista.begin() + 1, lista.end()), subconjuntos, lista_subconjuntos, k - 1);
    subconjuntos.pop_back();
    listasCombinatorias(vector<float>(lista.begin() + 1, lista.end()), subconjuntos, lista_subconjuntos, k);
}

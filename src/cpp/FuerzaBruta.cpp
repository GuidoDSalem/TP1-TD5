#include "include/FuerzaBruta.hpp"

float fuerzaBrutaRecursiva(
    vector<float> &gridX,
    vector<float> &gridY,
    vector<float> &xs,
    vector<float> &ys,
    vector<float> &resX,
    vector<float> &res,
    float bestError_,
    int k,
    const json &datos)
{

    //CASOS BASE

    if( k == 0 ){
        if(xs[0] != gridX[0]){
            return 100000001;
        }
        if(xs[xs.size()-1] != gridX[gridX.size()-1]){
            return 100000001;
        }

        for(int i=0; i< xs.size()-2;i++){
            if(xs[i] > xs[i+1] ){
                return 100000001;
            }
        }

        float error = errorBreakPoint(xs,ys,datos);

        if(error < bestError_){
            /*std::cout<<"ERROR: "<<error;
            printVector(&ys, " - BEST YS: ");
            */
            // res = ys;
            res.clear();
            resX.clear();
            for(int i=0;i < ys.size();i++){
                res.push_back(ys[i]);
                resX.push_back(xs[i]);
            }
            
            


            return error;
        }
        return bestError_;
    }


    //PASO RECURSIVO
    float bestError = bestError_;
    float error;

    for(int i=0; i<gridX.size();i++){
        xs.push_back(gridX[i]);
        for(int j=0; j< gridY.size();j++){
            //TODO
            ys.push_back(gridY[j]);
            error = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,resX,res,bestError,k-1,datos);

            if(error < bestError){
                bestError = error;
            }
            
            ys.pop_back();

        }
        xs.pop_back();
    }

    return bestError;

}

Result_t fuerzaBruta(int m, int n, int k, const json &data)
{
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

    vector<float> xs;
    vector<float> resX;
    vector<float> ys;
    vector<float> resY;

    float bestError = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,resX,resY,10000001,k,data);

    // res.bestError = bestError;
    
    auto fin = high_resolution_clock::now();
    double totalTime = (double)duration_cast<duration<double>>(fin - inicio).count();


    // devolvemos un struct con todas las respuestas
    Result_t res = {bestError, resX, resY, static_cast<float>(totalTime)};
    return res;
    }

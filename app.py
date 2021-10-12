import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/test_interseguro_api/', methods = ['POST'])
def processMatrix():
    try:        
        if 'application/json' in request.headers['content-type']:
                matrix = list(request.json['matrix'])
        else:
            return Response(status = 415)
        matriz = rotate_matrix(matrix)
        print(type(matriz))
        jsonResponse = {"Matriz" : matriz}
        return jsonResponse
        
    except Exception as e:
        return 'Ocurrio un error en la API.\n Error: {}\n'.format(e)

def rotate_matrix(matrix):
    if matrix is None or len(matrix) < 1:
            return 'Matrix invalida'
    else:
        n = len(matrix)
        for row in matrix:
            row.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
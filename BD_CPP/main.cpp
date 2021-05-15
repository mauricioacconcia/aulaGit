#include <iostream>
#include<windows.h>
#include<mysql.h>

const char* hostname = "localhost";
const char* username = "root";
const char* password = "12345678";
const char* database = "topicosavc";
unsigned int port = 3306;
const char* unixsocket = NULL;
unsigned long clientflag = 0;


using namespace std;

int main()
{
    MYSQL* conn;
    conn = mysql_init(0);
    conn = mysql_real_connect(conn, hostname, username, password, database, port, unixsocket, clientflag);
    cout << "Hello world!" << endl;
    if(conn){
        cout<<"Conexao Estabelecida"<<endl;
    }else{
        cout<<"Não foi possível realizar a conexão"<<endl;
    }
    return 0;
}

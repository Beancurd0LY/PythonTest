#/usr/bin/python
#encoding:utf-8


class MATRIX_ENV_CONF(object):

    def create_MATRIX_ENV_CONF(self):
        config = [
            '#[base]\n',
            'IDC = jx\n',
            'PORT = 9813\n',
            'JMXPORT = 11189\n',
            'IPADDR = 10.8.1.159\n',
            'IPADDR = 10.8.1.159\n',
            'HOSTNAME = normandy-biz.off.zhidaovip.com\n',
            'MATRIX_CACHE_DIR = \"/data0/www/cache/normandy-biz.off.zhidaovip.com/\"\n'
            'MATRIX_PRIVDATA_DIR = \"/data0/www/privdata/normandy-biz.off.zhidaovip.com/\"\n',
            'MATRIX_APPLOGS_DIR = \"/data0/www/applogs/normandy-biz.off.zhidaovip.com/\"\n',
            'MATRIX_ACCESSLOGS_DIR = \"/data0/www/logs/normandy-biz.off.zhidaovip.com/\"\n',
            '#[mysql]\n',
            'MATRIX_DB1_HOST = 10.8.1.184\n',
            'MATRIX_DB1_HOST_R = 10.8.1.184\n',
            'MATRIX_DB1_NAME = zhidao\n',
            'MATRIX_DB1_NAME_R = zhidao\n',
            'MATRIX_DB1_PORT = 3306\n',
            'MATRIX_DB1_PORT_R = 3306\n',
            'MATRIX_DB1_USER = zhidao\n',
            'MATRIX_DB1_USER_R = zhidao\n',
            'MATRIX_DB1_PASS = zhidao108679\n',
            'MATRIX_DB1_PASS_R = zhidao108679\n',
            '#[redis]\n',
            'MATRIX_REDIS1_HOST = "10.8.1.11:7010"\n',
            '#MATRIX_REDIS2_HOST = "10.8.1.11:7011"\n',
            '#MATRIX_REDIS3_HOST = "10.8.1.11:7012"\n']
        
        with open("MATRIX_ENV_CONF.ini","w") as f:
            for i in range(len(config)):
                f.write(config[i])


if __name__ == '__main__':
    a = MATRIX_ENV_CONF()    
    a.create_MATRIX_ENV_CONF()  
    
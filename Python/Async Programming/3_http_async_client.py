import requests, random
import asyncio

def multi_req(hostname:str, port:int, api_endpoint:str, arg_list:list):
    endpoint_prefix=f'http://{hostname}:{port}/{api_endpoint}/'
    for arg in arg_list:
        uri = endpoint_prefix
        count=0
        for key in arg:
            if count == 0:
                uri+=f'?{key}={arg[key]}'
            else:
                uri+=f'&{key}={arg[key]}'
            count+=1
        print(f'Requesting: {uri}')
        response=requests.get(uri)
        print(response.text)

async def req_async(uri):
    return requests.get(uri).text

async def multi_req_async(hostname:str, port:int, api_endpoint:str, arg_list:list):
    endpoint_prefix=f'http://{hostname}:{port}/{api_endpoint}/'
    uri_list=[]
    for arg in arg_list:
        uri = endpoint_prefix
        count=0
        for key in arg:
            if count == 0:
                uri+=f'?{key}={arg[key]}'
            else:
                uri+=f'&{key}={arg[key]}'
            count+=1
        uri_list.append(uri)

    response=await asyncio.gather(*[req_async(uri) for uri in uri_list])
    print(response.text)

def main():
    title_list=['abc', 'pqr', 'def']  # dummy title set
    time_range=(1,5) # time range 
    num_of_req=10
    arg_list=[]

    for req in range(num_of_req):
        title = title_list[random.randint(0,len(title_list)-1)]
        time = random.randint(*time_range)
        arg_list.append( {'title':title, 'time':time} )

    multi_req_async(hostname='localhost', port=5000, api_endpoint='dummy_api', arg_list=arg_list)

if __name__ == '__main__':
    main()
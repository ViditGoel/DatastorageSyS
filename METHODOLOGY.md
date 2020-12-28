<H1 align="center"> METHODOLOGY </H1>


> * Run [web app](https://github.com/ViditGoel/DatastorageSyS/blob/main/DATASTORAGE_SYS/web_app.py).
> * [Web app](https://github.com/ViditGoel/DatastorageSyS/blob/main/DATASTORAGE_SYS/web_app.py) works with html templates and use **GET** and **POST** methods with of [Flask](https://pythonbasics.org/what-is-flask-python/#:~:text=%20What%20is%20Flask%3F%20%201%20WSGI.%20The,keep%20the%20core%20of%20the%20application...%20More%20).
> * After running [web app](https://github.com/ViditGoel/DatastorageSyS/blob/main/DATASTORAGE_SYS/web_app.py) it will show "NOT FOUND ERROR ON LOCAL HOST" so, we have to use **APIs URL**.
    ```
    1. FOR CREATE localhost/CRD/create
    ```    
    ```
    2. FOR READ localhost/CRD/read
    ```
    ```
    3. FOR DELETE localhost/CRD/delete
    ```
> * [CRD](https://github.com/ViditGoel/DatastorageSyS/blob/main/DATASTORAGE_SYS/CRD.py) do all works of **CREATE,** **READ,** **DELETE** ,client functions(**LOCK,** **MULTIPROCESSING**) and check data integrity using [check data](https://github.com/ViditGoel/DatastorageSyS/blob/main/DATASTORAGE_SYS/check_data.py).

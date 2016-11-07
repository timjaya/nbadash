# Copy remote database to local

1. Dump remote database:

    ```bash
    $ pg_dump -U uni -h 104.196.175.120 postgres -n uni > ~/Desktop/backup.sql
    ```

2. Stop postgre

    ```bash
    $ sudo -u postgres bash -c 'killall postgres'
    ```

3. Set environment variables:

    a. Create environment file:

        $ touch ~/.bashrc
        $ vim ~/.bashrc

    b. Edit content:

        # this goes into ~/.bashrc
        export PGDATA=/home/<YOUR USERNAME>/pgdata
        export PGPORT=5432

        # this makes sure the installed posgresql tools are available in the shell
        export PATH=/usr/lib/postgresql/9.3/bin:$PATH

    c. Reload bashrc

    ```bash
    $ source ~/.bashrc
    ```

4. Allocate the files that PostgreSQL will use into the $PGDATA directory:

    ```bash
    $ initdb -D $PGDATA
    ```

5. Edit configuration file:

    ```bash
    $ vim $PGDATA/postgresql.conf
    ```

    At around line 59, uncomment the two options:

        listen_addresses = 'localhost'
        port = 5432

6. Start | restart | stop DBMS:

    ```bash
    $ pg_ctl start | restart | stop
    ```

7. Create a database:

    ```bash
    $ createdb test
    ```

8. Import dump file into database:

    ```bash
    $ psql test < backup.sql
    ```

9. In python server, set

        DATABASEURI = 'postgresql:///test'

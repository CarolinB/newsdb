# About newsdb.py

It is a simple program designed for magazines or newspapers to print the output on  the 3 following questions to the console:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of all requests lead to errors?

The program is written in Python, using a relational DB and PostgreSQL.

# Database

To test the program you can download a sample database here -

[Test Database .zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

The Test Database consists of 3 tables:

* articles
* authors
* log

The SQL queries in the code use JOIN on articles and authors, and, on articles and log. If you want to use this program with your own database be sure to adjust the table and column names in the SQL queries accordingly.

# Installation/Environment

Requires Python 2.7 and PostgreSQL version 9.5.x.

We recommend using this program in a virtual environment. If you like to do so follow the steps listed here:

## Install Virtual Machine

### Install Virtual Box

Here's a [Download Link](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) where you can download the latest version of VB. If you need help installing and getting started with VB check out the [Official Documentation](https://www.virtualbox.org/manual/ch02.html#intro-installing).

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

**Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install vagrant

You can download vagrant [here](https://www.vagrantup.com/downloads.html) and install the version for your OS.

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

### VM Configuration

You can download a .zip file with VM configuration files [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

Then follow the following steps using your terminal:

* `cd` to the VM config folder (if you didn't change the name it's called `FSND Virtual Machine`)
* direct into the vagrant folder `$ cd vagrant/`
* start vagrant `$ vagrant up` (this will install Linux OS)
* log in to Linux VM with `$ vagrant ssh`

## Connect the Database

* `$ cd vagrant/`
* `psql -d news -f newsdata.sql`

## Run the program

`$ python newsdb.py`

# Output example

```
Most popular 3 articles of all time:

"Candidate is jerk, alleges rival" - 342102 views
"Bears love berries, alleges bear" - 256365 views
"Bad things gone, say good people" - 171762 views

Most popular article authors of all time:

Ursula La Multa" - 512805
Rudolf von Treppenwitz" - 427781
Anonymous Contributor" - 171762
Markoff Chaney" - 85387

Days with more than 1% of all requests leading to errors:

Jul 17, 2016 - 2.26
```

# Licence

No licence required.

# Help

For any questions please send a message to our [support](mailto:carolin.bruederle@gmail.com).

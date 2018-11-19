pipeline{
agent any
    stages {
        stage("test") {
            steps {
                bat 'echo liron >> name_test.txt'
            }
        }
        stage("2") {
            steps {
                bat 'type name_test.txt'
            }
        }
        stage("3") {
            steps {
                bat 'fsutil volume diskfree c:'
            }
        }
        stage("4") {
            steps {
                bat 'move name_test.txt C:\Users\lirov\Documents'
            }
        }
    }
}
# Application-Web-base-sur-API-Apache-KAFKA-Stream
Il s’agit de développer une application Web basée sur l’API Apache KAFKA Stream, permettant de faire  l’analyse des données, dans le but de « prédire en temps réel le désabonnement des clients d’une entreprise »

![image](https://github.com/ouidadoualhaj/Application-Web-base-sur-API-Apache-KAFKA-Stream/assets/97354112/bab190e7-56ff-4ad3-8349-d301c02361bf)
   
Outils de travail : 

    • Librairies : Apache Kafka Stream, PySpark Mlib, Sklearn, Pytorch, Pandas, Matplotlib . 
  
    • Frameworks : Flask, Django 
  
    • Langages : Python, Java, Java Script … 
  
    • Editeurs : IntelliJ IDEA, Eclipse, VsCode 
  
    • Systèmes d’exploitation : Unix, MacOS ou Windows … 

Démarche à suivre : 

1-Installation KAFKA :

    -Avoir Java jdk bien installé
    
    -installer kafka de site officiel 
    
    -extraire l'archive installé et Extrayez le contenu du fichier téléchargé dans un répertoire de votre choix
    
    -ouvrir les deux fichiers server et zookeeper dans un IDE et modifier le path de dossier kafka (ex: C:/kafka/server)
    
    -ouvrir CMD dans le dossier kafka est exécuter les commandes suivantes: 
    
         C:\kafka>.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
         
         C:\kafka>.\bin\windows\kafka-server-start.bat .\config\server.properties
         
    -Créer nouveau Topic dans le répertoire kafka avec la commande:
    
         C:\kafka\bin\windows>kafka-topics.bat --create --bootstrap-server localhost:9092 --topic customer_churn
         
2-Installation des librairies nécessaires: pandas scikit-learn flask kafka-python pyspark ....

    -exécuter cette commande sur Jupyter : pip install pandas scikit-learn flask kafka-python pyspark
   
3-Lancer en temps réel les données avec Apache Kafka Streams (KafkaProducer) .

4-lire et Prétraiter les données avec Apache Kafka Streams (KafkaConsumer).

5-Entraînement des modèles ML supervisés (RandomForestClassifier, SVC, GradientBoostingClassifier) sur les données chargées de kafka.

6-Evaluer les trois modèle et Choisir le meilleur modèle puis l'enregistrer en utilisant la bibliothèque Joblib.

7-prédire en temps réel si le client quittera l’institution ou non sur les données de test : new_customers.csv

8-Présenter les résultats sous forme d’un tableau de bord d’une application Web (déploiement du modèle)

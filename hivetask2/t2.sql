ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-serde.jar;

USE tochilinvl;

SELECT request_time, count(request_time) AS cnt
FROM Logs GROUP BY request_time ORDER BY cnt DESC;

ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-contrib.jar;
ADD JAR /opt/cloudera/parcels/CDH/lib/hive/lib/hive-serde.jar;

USE tochilinvl;

SELECT IPRegions.region, COUNT(CASE WHEN Users.gender = "male" THEN 1 ELSE NULL END) AS male_cnt, COUNT(CASE WHEN Users.gender = "female" THEN 1 ELSE NULL END) AS fem_cnt
FROM Users INNER JOIN IPRegions ON (Users.ip = IPRegions.ip) GROUP BY IPRegions.region;

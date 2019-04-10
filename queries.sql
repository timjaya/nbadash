
-- Team Record: home

WITH team_select AS
(SELECT 'Boston Celtics' as team),
wins_location AS (
SELECT 
	sum(CASE WHEN home_team = (SELECT * FROM team_select) AND home_points > away_points THEN 1 ELSE 0 END) AS home_wins,
	sum(CASE WHEN home_team = (SELECT * FROM team_select) AND home_points < away_points THEN 1 ELSE 0 END) AS home_losses,
	sum(CASE WHEN away_team = (SELECT * FROM team_select) AND home_points < away_points THEN 1 ELSE 0 END) AS away_wins,
	sum(CASE WHEN away_team = (SELECT * FROM team_select) AND home_points > away_points THEN 1 ELSE 0 END) AS away_losses
FROM Team_Plays
)
SELECT home_wins + away_wins AS total_wins, home_losses + away_losses AS total_losses, *
FROM wins_location;


-- Team's last 5 Games

WITH team_select AS
(SELECT 'Boston Celtics' as team),
temp AS(
SELECT date_time_start::date as date,
	   CASE WHEN home_team = (SELECT * FROM team_select) THEN 'Home' ELSE 'Away' END AS home,
	   CASE WHEN home_team = (SELECT * FROM team_select) THEN away_team ELSE home_team END AS opponent,
	   stadium,
	   CASE WHEN home_team = (SELECT * FROM team_select) THEN home_points ELSE away_points END AS team_points,
	   CASE WHEN home_team = (SELECT * FROM team_select) THEN away_points ELSE home_points END AS opponent_points
FROM Team_Plays
WHERE home_team = (SELECT * FROM team_select) OR away_team = (SELECT * FROM team_select)
)
SELECT *, CASE WHEN team_points > opponent_points THEN 'W' ELSE 'L' END AS result
FROM temp
ORDER BY date DESC
LIMIT 5;


-- Player last 5 games

WITH player_select AS 
(SELECT 244 as pid)
SELECT 
    pn.pid,
	CASE WHEN t.home_team = p.team THEN away_team ELSE home_team END AS opponent,
	minutes_played, points, assists, rebounds, steals, blocks, turnovers,
	CASE 
		WHEN t.home_team = p.team AND home_points > away_points THEN 'W'
		WHEN t.away_team = p.team AND home_points < away_points THEN 'W'
		ELSE 'L' END AS result
FROM Player_Plays p
JOIN Team_Plays t on p.gid = t.gid
JOIN Player pn ON p.pid = pn.pid
WHERE p.pid = (SELECT * FROM player_select)
ORDER BY t.date_time_start DESC
LIMIT 5;

-- Player by distance

WITH player_select AS
(SELECT 244 as pid),
master as(
SELECT pp.*, t.stadium as home_stadium, tp.stadium as game_stadium, sd.distance as distance
FROM Player_Plays pp
JOIN Team t ON pp.team = t.name
JOIN Team_Plays tp ON tp.gid = pp.gid
JOIN Stadium_Distance sd ON sd.stadium_1 = t.stadium AND sd.stadium_2 = tp.stadium
WHERE pp.pid = (SELECT * FROM player_select)
),
master2 as (
SELECT 
	CASE 
		WHEN distance = 0 THEN 1
		WHEN distance < 500 THEN 3
		WHEN distance < 1000 THEN 4
		WHEN distance < 2000 THEN 5
		ELSE 6 END AS index,
	CASE 
		WHEN distance = 0 THEN 'At home'
		WHEN distance < 500 THEN '< 500 miles'
		WHEN distance < 1000 THEN '500-999 miles'
		WHEN distance < 2000 THEN '1,000-1,999 miles'
		ELSE '2,000+ miles' END AS distance_from_home,
	count(distinct gid) as games,
	avg(minutes_played) as mpg,
	avg(points) as ppg,
	avg(rebounds) as rpg,
	avg(assists) as apg,
	avg(steals) as spg,
	avg(blocks) as bpg,
	avg(turnovers) as topg,
	sum(fgm::float) as fgm,
	sum(fga::float) as fga,
	sum(threepm::float) as threepm,
	sum(threepa::float) as threepa
FROM master
GROUP BY 1,2)
SELECT distance_from_home, games, mpg, ppg, rpg, apg,
		CASE WHEN fga > 0 THEN fgm/fga ELSE 0 END AS fg_pct, 
		CASE WHEN threepa > 0 THEN threepm/threepa ELSE 0 END AS three_pct
FROM master2
ORDER BY index;

-- Head to Head: Stats for Player 1 vs PLayer 2

WITH player1 AS 
(SELECT 244 as pid),
player2 AS 
(SELECT 158 as pid),
games as (
SELECT p1.*
FROM (SELECT * FROM Player_Plays WHERE pid = (SELECT * FROM player1)) p1
JOIN (SELECT * FROM Player_Plays WHERE pid = (SELECT * FROM player2)) p2 
		ON p1.gid = p2.gid
),
stats as (
SELECT 
	count(distinct gid) as games,
	avg(minutes_played) as mpg,
	avg(points) as ppg,
	avg(rebounds) as rpg,
	avg(assists) as apg,
	avg(steals) as spg,
	avg(blocks) as bpg,
	avg(turnovers) as topg,
	sum(fgm::float) as fgm,
	sum(fga::float) as fga,
	sum(threepm::float) as threepm,
	sum(threepa::float) as threepa
FROM games
)
SELECT games, mpg, ppg, rpg, apg,
		CASE WHEN fga > 0 THEN fgm/fga ELSE 0 END AS fg_pct, 
		CASE WHEN threepa > 0 THEN threepm/threepa ELSE 0 END AS three_pct
FROM stats;

-- Head to Head: Player 1 vs Team

WITH player1 AS 
(SELECT 244 as pid),
team1 AS 
(SELECT 'Philadelphia 76ers' as pid),
games as (
SELECT p1.*
FROM (SELECT * FROM Player_Plays WHERE pid = (SELECT * FROM player1)) p1
JOIN (SELECT * FROM Team_Plays WHERE home_team = (SELECT * FROM team1) OR away_team = (SELECT * FROM team1)) t1 
		ON p1.gid = t1.gid
),
stats as (
SELECT 
	count(distinct gid) as games,
	avg(minutes_played) as mpg,
	avg(points) as ppg,
	avg(rebounds) as rpg,
	avg(assists) as apg,
	avg(steals) as spg,
	avg(blocks) as bpg,
	avg(turnovers) as topg,
	sum(fgm::float) as fgm,
	sum(fga::float) as fga,
	sum(threepm::float) as threepm,
	sum(threepa::float) as threepa
FROM games
)
SELECT games, mpg, ppg, rpg, apg,
		CASE WHEN fga > 0 THEN fgm/fga ELSE 0 END AS fg_pct, 
		CASE WHEN threepa > 0 THEN threepm/threepa ELSE 0 END AS three_pct
FROM stats;

-- Head to Head: Season Average for Player 1

WITH player1 AS 
(SELECT 244 as pid),
games as (
SELECT p1.*
FROM Player_Plays p1 
WHERE pid = (SELECT * FROM player1)
),
stats as (
SELECT 
	count(distinct gid) as games,
	avg(minutes_played) as mpg,
	avg(points) as ppg,
	avg(rebounds) as rpg,
	avg(assists) as apg,
	avg(steals) as spg,
	avg(blocks) as bpg,
	avg(turnovers) as topg,
	sum(fgm::float) as fgm,
	sum(fga::float) as fga,
	sum(threepm::float) as threepm,
	sum(threepa::float) as threepa
FROM games
)
SELECT games, mpg, ppg, rpg, apg,
		CASE WHEN fga > 0 THEN fgm/fga ELSE 0 END AS fg_pct, 
		CASE WHEN threepa > 0 THEN threepm/threepa ELSE 0 END AS three_pct
FROM stats;



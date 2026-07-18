SELECT  id AS id_teams,
        full_name AS team_name,
        abbreviation,
        nickname,
        city,
        state,
        year_founded
FROM {{ ref('teams') }}
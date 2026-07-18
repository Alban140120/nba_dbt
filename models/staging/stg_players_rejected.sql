SELECT id AS id_players,
    full_name AS player_name,
    first_name,
    last_name,
    is_active
from {{ ref('players') }}
where full_name IS NULL

with open("three/input.txt", "r") as claims_file:
    claims = [claim.strip() for claim in claims_file.readlines()]
    parsed_claims = [] # format (id, [loc.x, loc.y], [size.x, size.y])

    # parse claims
    for claim in claims: # claim format "#??? @ ?,?: ?x?"
        at_index = claim.index("@")
        colon_index = claim.index(":")

        claim_id = claim[1:at_index - 1] # -1 to remove whitespace
        claim_loc = claim[at_index + 2:colon_index] # +1 to get rid of @, +1 to remove whitespace
        claim_size = claim[colon_index + 2:] # +1 to remove colon, +1 to remove whitespace

        parsed_claim = (claim_id, claim_loc.split(","), claim_size.split("x"))
        parsed_claims.append(parsed_claim)

    grid = {}
    # populate fabric "grid"
    for claim in parsed_claims:
        org_x = int(claim[1][0])
        org_y = int(claim[1][1])
        width = int(claim[2][0])
        height = int(claim[2][1])

        # populate grid cells with the ID of the owning claim, or X for an overlap
        for x in range(org_x, org_x + width):
            if (x not in grid):
                grid[x] = {}

            for y in range(org_y, org_y + height):
                if (y not in grid[x]):
                    grid[x][y] = claim[0]
                else:
                    grid[x][y] = "X"

    # check grid for overlaps
    overlaps = 0
    for column in grid.keys():
        for cell in grid[column].values():
            if (cell == "X"):
                overlaps += 1
    
    print("Overlaps: {}".format(overlaps))
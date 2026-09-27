label INIT_INVENTORY_ITEMS:
    python:
        sea_dogs_saga = ComicItem("game", "Sea Dogs SAGA", "", 'game_1', 'game_1b', 100, "Video Games", False, None, sea_dogs_saga_callback)
        world_of_orcette = ComicItem("game02", "World of Orcette", "", 'game_2', 'game_2b', 100, "Video Games", False, None, world_of_orcette_callback)
        orcette_outfit = ComicItem("orcette_cosplay", "Orcette Queen Garments", "", Transform("cosplay_1"), Transform("cosplay_1b"), 300, "Cosplay", False, None, orc_cosplay_callback)
        cyclone_mask = ComicItem("cyclone_mask", "Pink Cyclone Mask", "", "objects/item_mask1.png", HoverImage("objects/item_mask1.png"), 100, "Cosplay", False, "M_jenny.finished_state(S_jenny_get_a_mask)", cyclone_mask_callback)
        cock_goblin = ComicItem("card01", "Trading Card - The Flying Cock Goblin", "objects/closeup_card01.png", "objects/item_card1.png", HoverImage("objects/item_card1.png"), 50, "Collectible")
        cock_crown = ComicItem('card02', 'Trading Card - Cock Crown of Thorns', 'objects/closeup_card02.png', 'card_2', 'card_2b', 50, 'Collectible', False, None, ccot_callback)

        comicstore = ComicStore()
        comicstore.items = [cock_goblin, sea_dogs_saga, world_of_orcette, cock_crown, orcette_outfit, cyclone_mask]

        red_corset_lingerie = PinkItem("red_corset", "The Ruby Corset", "", "sex_17", "sex_17b", 300, "Lingerie", False)
        cow_outfit_lingerie = PinkItem("cow_outfit", "The Milk Slave", "", "sex_6", "sex_6b", 300, "Lingerie", False)

        pinkstore = PinkStore()
        pinkstore.items = [red_corset_lingerie, cow_outfit_lingerie]

        plush1 = CupidItem("plush_1", "Plush - Awesomo", "Plushes")
        plush2 = CupidItem("plush_2", "Plush - Pinguin", "Plushes")
        plush3 = CupidItem("plush_3", "Plush - Kitty", "Plushes")
        plush4 = CupidItem("plush_4", "Plush - Cow", "Plushes")
        plush5 = CupidItem("plush_5", "Plush - Otter", "Plushes")
        plush6 = CupidItem("plush_6", "Plush - Rabbit", "Plushes")
        plush7 = CupidItem("plush_7", "Plush - Unicorn", "Plushes")
        plush8 = CupidItem("plush_8", "Plush - Orcette", "Plushes")
        plush9 = CupidItem("plush_9", "Plush - Panda", "Plushes")
        plush10 = CupidItem("plush_10", "Plush - Barbarian", "Plushes")
        plush11 = CupidItem("plush_11", "Plush - Pink Beaver", "Plushes")
        plush12 = CupidItem("plush_12", "Plush - Snecko", "Plushes")
        chocolates = CupidItem("chocolates", "Chocolates", "Plushes", callback=cupid_chocolates_callback)

        flower1 = CupidItem("flower_1", "Flowers - Lillies", "Flowers")
        flower2 = CupidItem("flower_2", "Flowers - Daisies", "Flowers")
        flower3 = CupidItem("flower_3", "Flowers - Roses", "Flowers")
        flower4 = CupidItem("flower_4", "Flowers - Callas", "Flowers")
        flower5 = CupidItem("flower_5", "Flowers - Orchids", "Flowers")
        flower6 = CupidItem("flower_6", "Flowers - Tulips", "Flowers")
        flower7 = CupidItem("flower_7", "Flowers - Sunflowers", "Flowers")

        necklace1 = CupidItem("pearl_necklace", "Necklace - Pearl", "Jewelery")
        necklace2 = CupidItem("heart_necklace", "Necklace - Heart", "Jewelery")
        necklace3 = CupidItem("crystal_necklace", "Necklace - Crystal", "Jewelery")

        cupidstore = CupidStore()
        cupidstore.items = [plush1, plush2, plush3, plush4, plush5, plush6, plush7, plush8, plush9,
                            plush10, plush11, plush12, flower1, flower2, flower3, flower4, flower5,
                            flower6, flower7, necklace1, necklace2, necklace3, chocolates]
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

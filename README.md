# Lien heroku
    * https://scrappproject.herokuapp.com/ 



# Models et champs

    * Source
        - name : CharField
        - link : URLField
    
    * Article
        - title : TextField
        - picture : TextField
        - date_publication : TextField
        - link_detail : TextField
        - description : HTMLField
        - source : Foreignkey(Source)
        - category : Foreignkey(Categorie)
        - tag : Foreignkey(Tag)
    
    * Category
        - name : CharField
    
    * Tag
        - name : CharField

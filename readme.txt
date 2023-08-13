# GraphQL approach description

To add new entities and capabilities the approach that has worked here is: 

1. Add the new model. The model must include the fields, types, relational keys to other entities. Then it must define how back population works. This is the relationship to other entities as follows: identified = relationship("OtherEntity", back_populates="this-entity", lazy="joined").
2. Add the types to the file holding the SQLAlchemy types. These should have fileds with the relationship defined and (lambda: RelatinshipEntity) defined as well as resolvers for these fields.
3. Any sample data/initial load can be added to the db setup/upgrade/cutover script. 
4. Add the related queries and mutations to the appropriate folders
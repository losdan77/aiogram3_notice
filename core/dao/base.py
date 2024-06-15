from database import async_session_maker
from sqlalchemy import insert, select, delete, update, text
from datetime import date


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def update(cls, id_user: str, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(
                                            cls.model.id == id, 
                                            cls.model.id_user == id_user).values(**data)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def select_all_id_user(cls):
        async with async_session_maker() as session:
            query = select(cls.model.id_user)
            result = await session.execute(query)
            return result.mappings().all()
    

    @classmethod
    async def select_by_id(cls, id_user: str):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id_user=id_user)
            result = await session.execute(query)
            return result.mappings().all()

    
    @classmethod
    async def select_by_id_date_standard_notice(cls, id_user: str, date_world: date):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id_user=id_user,
                                                                  date_notice=date_world,
                                                                  id_type=3)
            result = await session.execute(query)
            return result.mappings().all()
        
    
    @classmethod
    async def select_by_id_date_birthday_notice(cls, id_user: str, date_world: str):
        async with async_session_maker() as session:
            query = f"select * from accouting_notice where date_birthday::varchar like '%-{date_world}' and id_user = '{id_user}' and id_type = 1"
            result = await session.execute(text(query))
            return result.mappings().all()
        
    
    @classmethod
    async def select_by_id_date_pay_notice(cls, id_user: str, date_world: str):
        async with async_session_maker() as session:
            query = f"select * from accouting_notice where date_notice::varchar like '%-{date_world}' and id_user = '{id_user}' and id_type = 2"
            result = await session.execute(text(query))
            return result.mappings().all()
        
    
    @classmethod
    async def select_by_id_type(cls, id_user: str, id_type: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id_user=id_user, id_type=id_type)
            result = await session.execute(query)
            return result.mappings().all()
        
    
    @classmethod
    async def delete_by_id(cls, id_user: str, id: int):
        async with async_session_maker() as session:
            query_select = select(cls.model).filter_by(id=id, id_user=id_user)
            result_select = await session.execute(query_select)

            if result_select.scalar():
                query_delete = delete(cls.model).where(cls.model.id == id,
                                                       cls.model.id_user == id_user)
                result_delete = await session.execute(query_delete)
                await session.commit()
                return 'seccessful'
            else:
                return None
            

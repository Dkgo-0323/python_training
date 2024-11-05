class Person() :
    def __init__(self,name) :
        self.name = name
    def get_name(self) :
        return self.name
person = Person("Bob")
name = person.get_name()
print(name)



class Movie:
    def __init__(self, name, seat_count=50, ticket_price=30):
        self.name = name
        self.seat_count = seat_count
        self.ticket_price = ticket_price
        self.available_seats = seat_count
        self.total_sales = 0

class TicketingMachine:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie_name):
        if movie_name not in self.movies:
            self.movies[movie_name] = Movie(movie_name)

    def sell_tickets(self, movie_name, num_tickets):
        if movie_name in self.movies:
            movie = self.movies[movie_name]
            if movie.available_seats >= num_tickets:
                movie.available_seats -= num_tickets
                revenue = num_tickets * movie.ticket_price
                movie.total_sales += revenue
                return f"成功售出 {num_tickets} 张票，总收入：{revenue} 元。"
            else:
                return "座位不足，无法完成购票。"
        else:
            return "找不到指定电影，无法完成购票。"

    def refund_tickets(self, movie_name, num_tickets):
        if movie_name in self.movies:
            movie = self.movies[movie_name]
            movie.available_seats += num_tickets
            refund_amount = num_tickets * movie.ticket_price
            movie.total_sales -= refund_amount
            return f"成功退还 {num_tickets} 张票，退款：{refund_amount} 元。"
        else:
            return "找不到指定电影，无法完成退票。"

    def display_total_sales(self):
        total_sales = sum(movie.total_sales for movie in self.movies.values())
        return f"总票房：{total_sales} 元。"

ticket_machine = TicketingMachine()
ticket_machine.add_movie("复仇者联盟：终结之战")
ticket_machine.add_movie("猫鼠游戏")

print(ticket_machine.sell_tickets("复仇者联盟：终结之战", 3))
print(ticket_machine.sell_tickets("猫鼠游戏", 2))
print(ticket_machine.sell_tickets("当幸福来敲门", 4))  
print(ticket_machine.sell_tickets("复仇者联盟：终结之战", 48))
print(ticket_machine.sell_tickets("复仇者联盟：终结之战", 3)) 

print(ticket_machine.refund_tickets("猫鼠游戏", 1))
print(ticket_machine.display_total_sales())

class Pagination:
    def __init__(self, total_items, items_per_page):
        self.total_items = total_items
        self.items_per_page = items_per_page
        self.current_page = 1

    def get_pages(self):
        total_pages = -(-self.total_items // self.items_per_page)  # integer division
        pages = []
        for i in range(1, total_pages + 1):
            pages.append(i)
        return pages

    def get_current_page(self):
        return self.current_page

    def get_previous_page(self):
        if self.current_page > 1:
            return self.current_page - 1
        return None

    def get_next_page(self):
        if self.current_page < self.get_pages()[-1]:
            return self.current_page + 1
        return None

    def change_page(self, page):
        if 1 <= page <= self.get_pages()[-1]:
            self.current_page = page
        else:
            raise ValueError("Invalid page number")

class PaginationComponent:
    def __init__(self, pagination):
        self.pagination = pagination

    def render(self):
        pages = self.pagination.get_pages()
        current_page = self.pagination.get_current_page()
        previous_page = self.pagination.get_previous_page()
        next_page = self.pagination.get_next_page()

        html = f"""
        <div class="pagination">
            <button class="page-btn" onclick="changePage({previous_page})">Previous</button>
            <button class="page-btn active" onclick="changePage({current_page})">{current_page}</button>
            <button class="page-btn" onclick="changePage({next_page})">Next</button>
        </div>
        """

        for page in pages:
            if page != current_page:
                html += f"""
                <button class="page-btn" onclick="changePage({page})">{page}</button>
                """

        return html

# Example usage:
pagination = Pagination(100, 10)
component = PaginationComponent(pagination)
print(component.render())
```

Bu kodda, `Pagination` klassi ma'lum miqdordagi ma'lum miqdorda ma'lumotlarni saqlash uchun mo'ljallangan. `PaginationComponent` klassi esa bu ma'lumotlarni HTML faylida ko'rsatish uchun mo'ljallangan. `render` metodi HTML faylida ko'rsatilgan ma'lumotlarni qaytaradi.

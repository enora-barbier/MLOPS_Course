from API_backend import get_surface_direct  # Direct function import

if __name__ == "__main__":
    surface_value = 42
    data = get_surface_direct(surface_value)  # No HTTP needed
    print(data)

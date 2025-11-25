#include <SFML/Graphics.hpp>
#include <iostream>

int main()
{
    // Create a video mode object (window size 800x600)
    sf::VideoMode videoMode(800, 600);

    // Create a render window
    sf::RenderWindow window(videoMode, "Move Rectangle with Arrow Keys");

    // Set the frame rate limit to make movement smoother
    window.setFramerateLimit(120);

    // Create a rectangle shape (size 100x50)
    sf::RectangleShape rectangle(sf::Vector2f(100.f, 50.f));

    // Set the rectangle's initial position
    rectangle.setPosition(350.f, 275.f); // Center of the window

    // Set the rectangle's fill color
    rectangle.setFillColor(sf::Color::Green);

    // Movement speed (pixels per frame)
    float movementSpeed = 5.0f;

    // Main game loop
    while (window.isOpen())
    {
        // Event polling (for handling window close, etc.)
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Real-time input for moving the rectangle
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
        {
            rectangle.move(0.f, -movementSpeed); // Move up
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
        {
            rectangle.move(0.f, movementSpeed); // Move down
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
        {
            rectangle.move(-movementSpeed, 0.f); // Move left
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
        {
            rectangle.move(movementSpeed, 0.f); // Move right
        }

        sf::Vector2 pos = rectangle.getPosition();
        std::cout << pos.x << " " << pos.y << std::endl;
        sf::Vector2u size = window.getSize();

        if (pos.x > size.x)
        {
            pos.x = -rectangle.getSize().x;
        }
        else if (pos.x + rectangle.getSize().x < 0)
        {
            pos.x = size.x;
        }

        if (pos.y > size.y)
        {
            pos.y = -rectangle.getSize().y;
        }
        else if (pos.y + rectangle.getSize().y < 0)
        {
            pos.y = size.y;
        }

        rectangle.setPosition(pos);
        // Clear the window
        window.clear();

        // Draw the rectangle
        window.draw(rectangle);

        // Display the rendered frame
        window.display();
    }

    return 0;
}

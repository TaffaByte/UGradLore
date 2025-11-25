#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    // Create a window
    sf::RenderWindow window(sf::VideoMode(400, 300), "STOP Sign");
    window.setVerticalSyncEnabled(true);

    // Create the pole (rectangle)
    sf::RectangleShape pole(sf::Vector2f(30, 200));
    pole.setFillColor(sf::Color::Black);
    pole.setPosition(193, 100); // Centered under circle

    // Create the outer red
    sf::CircleShape circle(80);
    circle.setFillColor(sf::Color::White);       // White inner color
    circle.setOutlineThickness(20);              // Red border thickness
    circle.setOutlineColor(sf::Color::Red);
    circle.setPosition(130, 20);                 // Top position

    // Load font (make sure Arial.ttf is in the same folder)
    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        std::cout << "Error: Could not load font.\n";
        return -1;
    }

    // Create the STOP text
    sf::Text text;
    text.setFont(font);
    text.setString("STOP");
    text.setCharacterSize(50);
    text.setFillColor(sf::Color::Black);

    // Center the text inside the circle
    sf::FloatRect textRect = text.getLocalBounds();
    text.setOrigin(textRect.left + textRect.width / 2.0f,
                   textRect.top + textRect.height / 2.0f);
    text.setPosition(2, 100); // Circle center

    // Main loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::Cyan);  // Background color
        window.draw(pole);
        window.draw(circle);
        window.draw(text);
        window.display();
    }

    return 0;
}

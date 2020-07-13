////////////////////////////////////////////////////////////////////////////////////////
// INSTRUCTIONS:  
//    This exercise is to prepare Mission data so it can be handed to the UI. The 
//    data is not ready as-is, and will need some processing before it can be sent to
//    the UI. The mission data is stored in data.json .
//
//    This test relies on JSON for Modern C++:
//      See https://github.com/nlohmann/json for full details and documentation.
//      You are not expected to be familiar with this library already.  
//  
//    Feel free to write any helper methods you think are necessary.
//    However, DO NOT add any additional includes or libraries.  
//
//    Comments are appreciated but not required.  They might help us better understand
//    your thought process.  


/*

Since the mission data is NOT ready as-is, I take that as it needs to be changed
to make it ready. ---->>>>> rewite the json file.

***Insersion Sort*** is my choice


*/




////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////
// Don't change these
////////////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <fstream>
#include <cmath>

#include "nlohmann/json.hpp"

using json = nlohmann::json;

struct Vec2 {
	float x;
	float y;
	Vec2(float x, float y) : x(x), y(y) {}
};

const Vec2 player_pos(101.29f, 85.4298f);
////////////////////////////////////////////////////////////////////////////////////////

struct missionItem {
	std::string title = "";
	std::string desc = "";
	float x = 0.0;
	float y = 0.0;
	float distFromPlayer = 0.0;
};

////////////////////////////////////////////////////////////////////////////////////////
// YOUR CODE HERE: You're free to chose the sorting algorithm, but it should be 
//    appropriate for the problem.  You are expected to write this yourself
//    from scratch without using anything from <algorithm> or other libraries.
//
// Since the mission data is NOT ready as-is, I take that as it needs to be changed
// to make it ready. ---->>>> > rewite the json file.
//
// *** Insersion Sort*** is my choice
//
// EXPLAIN
//
//
////////////////////////////////////////////////////////////////////////////////////////
void Sort(json& list)
{
	// Converting the json list to vector list for easier sorting
	std::vector<missionItem> missionsContainer = convertFromJson(list);

	// Holding total number of missions
	int numMissions = list.at("missions").size();

	// Each new element will be inserted into the list at its creation
	std::vector<missionItem>::iterator it = missionsContainer.begin();

	// Key is first element distance in the list
	float key = it->distFromPlayer;

	// loop until a location in vector for new item is found
	while (it != missionsContainer.end())
	{			
		// If the current distance to player is less than or equal to key,
		// insert in place
		if (it->distFromPlayer <= key)
		{
			missionsContainer.insert(it, newItem);
		}
		// If the iterator is the last element, insert new item at end 
		else if (it == missionsContainer.end())
		{
			missionsContainer.insert(it, newItem);
		}
		// If the current distance to player is greater to key,
		// then it needs to go farther back in the list
		else if (it->distFromPlayer > key)
		{
			it++;
		}
	}

	for (auto it = missionsContainer.begin(); it != missionsContainer.end(); it++)
	{
		std::cout << "name: " << it->title << ". Dist: " << it->distFromPlayer << std::endl;
	}
}// END - Sort

void SendToUI(json& data)
{
	////////////////////////////////////////////////////////////////////////////////////////
	// YOUR CODE HERE: Imagine this is where the data gets handed off to the UI.
	//    For this test, just print out the mission data to the console in a clear way.
	////////////////////////////////////////////////////////////////////////////////////////
	std::cout << "SendToUI Called" << std::endl;
}// END - SendToUI

std::vector<missionItem> convertFromJson(json data)
{
	std::vector<missionItem> missionsContainer;

	// Holding total number of missions
	int numMissions = data.at("missions").size();

	for (int i = 0; i < numMissions; ++i) {
		missionItem newItem;

		// Capturing the title
		newItem.title = data.at("missions").at(i).at("title").dump();

		// Capturing the description
		newItem.desc = data.at("missions").at(i).at("desc").dump();

		// Capturing the x, y coords
		newItem.x = data.at("missions").at(i).at("position").at(0);
		newItem.y = data.at("missions").at(i).at("position").at(1);

		// Calculating distance between player_pos and newItem pos
		newItem.distFromPlayer = sqrt(pow((newItem.x - player_pos.x), 2)
			+ pow((newItem.y - player_pos.y), 2));

		// pushing new item
		missionsContainer.push_back(newItem);
	}

	return missionsContainer;
}// END - convertFromJson

void rewriteJaonData()
{

}// END - rewriteJsonData

int main()
{
	std::ifstream config_file("data.json");
	json data;
	config_file >> data;


	////////////////////////////////////////////////////////////////////////////////////////
	// YOUR CODE HERE:  
	//  - Missions should be sorted by distance from player_pos, nearest to farthest, by 
	//    calling Sort.
	//  - After that data has been fully prepared and sorted, pass it to SendToUI.
	//  - Think carefully about what data should be sent to the UI.
	////////////////////////////////////////////////////////////////////////////////////////

	try {

		Sort(data);
		//SendToUI(data);


	}
	catch (std::exception& e) {
		std::cout << e.what() << std::endl;
	}

	return 0;
}

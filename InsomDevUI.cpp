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

std::vector<missionItem> convertFromJson(json data)
{
	std::vector<missionItem> unsortedMissions;

	// Holding total number of missions
	int numMissions = data.at("missions").size();

	for (int i = 0; i < numMissions; ++i) {
		missionItem newItem;

		// Capturing the title
		newItem.title = data.at("missions").at(i).at("title").dump();

		// Capturing the description
		newItem.desc = data.at("missions").at(i).at("desc").dump();

		// Capturing the x, y coords
		newItem.x = data.at("missions").at(i).at("position").at(0).get<int>();
		newItem.y = data.at("missions").at(i).at("position").at(1).get<int>();

		// Calculating distance between player_pos and newItem pos
		newItem.distFromPlayer = sqrt(pow((newItem.x - player_pos.x), 2)
			+ pow((newItem.y - player_pos.y), 2));

		// pushing new item
		unsortedMissions.push_back(newItem);
	}

	return unsortedMissions;
}// END - convertFromJson


void printVector(std::vector<missionItem> vec)
{
	for (auto it = vec.begin(); it != vec.end(); it++)
	{
		printf("Title: %s, Desc: %s, (%f, %f), %f units from player.\n",
			it->title.c_str(), it->desc.c_str(), it->x, it->y, it->distFromPlayer);
	}
}

void rewriteJsonData(json &jsonData, std::vector<missionItem> sortedVec)
{
	// Holding total number of missions
	int numMissions = jsonData.at("missions").size();
	
	std::ofstream file("data.json");

	for (int i = 0; i < numMissions; ++i) {

		// Capturing the title
		jsonData.at("missions").at(i).at("title") = sortedVec[i].title;

		// Capturing the description
		jsonData.at("missions").at(i).at("desc") = sortedVec[i].desc;

		// Capturing the x, y coords
		jsonData.at("missions").at(i).at("position").at(0) = sortedVec[i].x;
		jsonData.at("missions").at(i).at("position").at(1) = sortedVec[i].y;
	}
	
	file << jsonData.dump(4);

	std::cout << jsonData << std::endl;

}// END - rewriteJsonData

////////////////////////////////////////////////////////////////////////////////////////
// YOUR CODE HERE: You're free to chose the sorting algorithm, but it should be 
//    appropriate for the problem.  You are expected to write this yourself
//    from scratch without using anything from <algorithm> or other libraries.
//
// Since the mission data is NOT ready as-is, I take that as it needs to be changed
// to make it ready. ---->>>> > rewite the json file.
//
// *** Insersion Sort*** is my choice Explain why used vectors, too.
//
// EXPLAIN
//
//
////////////////////////////////////////////////////////////////////////////////////////
void Sort(json& list)
{
	// Converting the json list to vector list for easier sorting
	std::vector<missionItem> missionsList = convertFromJson(list);

	// Holding total number of missions
	// int numMissions = list.at("missions").size();

	std::cout << "Unsorted" << std::endl;
	printVector(missionsList);
	std::cout << std::endl << std::endl;
	try {


		// looping through all elements in json vector
		for (std::vector<missionItem>::iterator it = missionsList.begin(); it != missionsList.end(); it++)
		{
			// Setting key to largest possible value for evaluation purposes
			float key = std::numeric_limits<float>::max();

			std::vector<missionItem>::iterator currHigh;

			for (std::vector<missionItem>::iterator itIn = it; itIn != missionsList.end(); itIn++)
			{
				// if current element is greater than key, set new key
				if (itIn->distFromPlayer <= key)
				{
					key = itIn->distFromPlayer;
					currHigh = itIn;
				}
			}
			std::rotate(it, currHigh, missionsList.end());
		}
	}
	catch (std::exception& e)
	{
		std::cout << e.what() << std::endl;
	}

	std::cout << "Sorted" << std::endl;
	printVector(missionsList);
	std::cout << std::endl << std::endl;

	rewriteJsonData(list, missionsList);

	std::cout << "End of sort" << std::endl;

}// END - Sort

void SendToUI(json& data)
{
	////////////////////////////////////////////////////////////////////////////////////////
	// YOUR CODE HERE: Imagine this is where the data gets handed off to the UI.
	//    For this test, just print out the mission data to the console in a clear way.
	////////////////////////////////////////////////////////////////////////////////////////
	std::cout << "SendToUI Called" << std::endl;
}// END - SendToUI

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

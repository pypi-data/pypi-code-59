from eo_lib.config.base import Entity
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, String, Text, Date
from sqlalchemy.orm import relationship
from eo_lib.model.relationship.models import *


class Organization(Entity):
	is_instance_of = "Organization"
	__tablename__  = "organization"
	configuration = relationship("Configuration", back_populates="organization") 

class Person(Entity):
	"""A human Physical Agent."""
	
	is_instance_of = "person"
	__tablename__  = "person"
	type = Column(String(50))
	
	email = Column(String(200))

	__mapper_args__ = {'polymorphic_identity':'team','polymorphic_on':type}
	

class TeamMember(Person):
	"""A Person allocated in a Team."""
	
	is_instance_of = "person"
	__tablename__  = "teammember"
	id = Column(Integer, ForeignKey('person.id'), primary_key=True)
	
	teammebership = relationship("TeamMembership", back_populates="teammember") 
	
	__mapper_args__ = {'polymorphic_identity':'teammember',}
	

class Organization_Role(Entity):
	"""A Social Role, recognized by the Organization, assigned to Agents when they are hired, included in a team, allocated or  participating in activities.Ex.: System Analyst, Designer, Programmer, 
		Client Organization."""
	
	is_instance_of = "organizational_role"
	__tablename__  = "organization_role"
	
	teammebership = relationship("TeamMembership", back_populates="organization_role") 
	

class TeamMembership(Entity):
	"""Relationship among Team member, organizational Role and team."""
	
	is_instance_of = "TeamMembership"
	__tablename__  = "teammembership"

	date = Column(Date)

	organization_role_id = Column(Integer, ForeignKey("organization_role.id"))
	organization_role = relationship("Organization_Role", back_populates="teammebership") 
			
	team_id = Column(Integer, ForeignKey("team.id"))
	team = relationship("Team", back_populates="teammebership") 
			
	teammember_id = Column(Integer, ForeignKey("teammember.id"))
	teammember = relationship("TeamMember", back_populates="teammebership") 
		
	

class Team(Entity):
	"""Social Agent representing a group of people with a defined purpose. 
		Ex.: a Testing team, a Quality Assurance team, a Deployment team."""
	
	is_instance_of = "Team"
	__tablename__  = "team"
	type = Column(String(50))

	teammebership = relationship("TeamMembership", back_populates="team") 
	__mapper_args__ = {'polymorphic_identity':'team','polymorphic_on':type}
	
class Project(Entity):
	"""A Social Object as a temporary endeavor undertaken to create a unique product, service, or result.
		Ex.: A project to produce a software on demand."""
	
	is_instance_of = "Project"
	__tablename__  = "project"
	
	team = relationship("ProjectTeam", back_populates="project") 

class ProjectTeam(Team):
	"""A Team with a project"""
	
	is_instance_of = "Team"
	__tablename__  = "projectteam"
	id = Column(Integer, ForeignKey('team.id'), primary_key=True)

	project_id = Column(Integer, ForeignKey('project.id'))
	project = relationship("Project", back_populates="team") 
		
	__mapper_args__ = {'polymorphic_identity':'projectteam',}	


	
